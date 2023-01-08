import argparse
import getpass

import pandas as pd
import requests
from tabulate import tabulate

# pip3 install tabulate pandas requests -i https://engci-maven-master.cisco.com/artifactory/api/pypi/apic-em-pypi-group/simple
# pip3 install Pillow -i https://engci-maven-master.cisco.com/artifactory/api/pypi/apic-em-pypi-group/simple

# Invocation: "python bdd_results_compare.py  -b 4715 -c NP2113"
# -b BASELINE_RUN -c CURRENT_RUN [-u USERNAME] [-p PASSWORD]
# Please check whether the build numbers are correct,
# if any one of the build numbers is from custom/non-production
# jenkins job please add 'NP' before build number Example: 'python bdd_results_compare.py  -b 4715 -c NP2113'


def get_urls(baseline_run_id, current_run_id):
    regression_run_job = "https://engci-private-sjc.cisco.com/jenkins/thunderbolt/job/"
    production_job = "assurance-it-regression-bdd-on-prem-in-docker/"
    non_production_job = "assurance-it-regression-bdd-on-prem-in-docker-non-production/"
    suites_csv = "/allure/data/suites.csv"
    report = "/allure/"

    # If the run is from a non-production job then remove 'NP' from the input string
    if "NP" in baseline_run_id:
        baseline_run_id = str(baseline_run_id).split("NP")[1]
        job = non_production_job
    else:
        job = production_job
    baseline_build_url = regression_run_job + job + str(baseline_run_id)
    baseline_run_url = baseline_build_url + report
    baseline_run_content_url = baseline_build_url + suites_csv

    if "NP" in current_run_id:
        current_run_id = str(current_run_id).split("NP")[1]
        job = non_production_job
    else:
        job = production_job
    current_build_url = regression_run_job + job + str(current_run_id)
    current_run_url = current_build_url + report
    current_run_content_url = current_build_url + suites_csv

    return [baseline_run_url, current_run_url, baseline_run_content_url, current_run_content_url]


def get_results(url_list, baseline_run_id, current_run_id, username, password):
    # Download the result content using urls and parse the content
    baseline_run_content_url, current_run_content_url = url_list[2], url_list[3]
    baseline_run_response = requests.get(baseline_run_content_url, auth=(username, password))
    current_run_response = requests.get(current_run_content_url, auth=(username, password))
    if baseline_run_response.status_code == 401 or current_run_response.status_code == 401:
        print("\n\nInvalid Credentials: ERROR 401 Unauthorized. Try your cisco credentials\n")
        quit()

    baseline_run_file = "suites_baseline.csv"
    current_run_file = "suites_current_run.csv"

    with open(baseline_run_file, "wb") as out:
        for bits in baseline_run_response.iter_content():
            out.write(bits)
    with open(baseline_run_file, "r") as out:
        if "Error 404 Not Found" in out.read():
            print("\n\n!!Baseline run build number({}) is incorrect".format(baseline_run_id))
            print(
                "\n!!!!!!Please check whether the build numbers are correct,"
                "if any one of the build numbers is from custom/non-production"
                "jenkins job please add 'NP' before build number Example: 'python bdd_results_compare.py 4622 NP1961'\n\n"
            )
            quit()

    with open(current_run_file, "wb") as out:
        for bits in current_run_response.iter_content():
            out.write(bits)
    with open(current_run_file, "r") as out:
        if "Error 404 Not Found" in out.read():
            print("\n\n!!Current run build number({}) is incorrect".format(current_run_id))
            print(
                "\n!!!!!!Please check whether the build numbers are correct,"
                "if any one of the build numbers is from custom/non-production"
                "jenkins job please add 'NP' before build number Example: 'python bdd_results_compare.py 4622 NP1961'\n\n"
            )
            quit()

    print("\nRegression Reports URL:")
    print("\nBaseline Run: ", str(url_list[0]))
    print("Current Run: ", str(url_list[1]))
    try:
        df_1 = pd.read_csv(baseline_run_file, usecols=["Name", "Status"])
        status_dict_1 = df_1.set_index("Name")["Status"].to_dict()
        # d1_keys = status_dict_1.keys()

        df_2 = pd.read_csv(current_run_file, usecols=["Name", "Status"])
        status_dict_2 = df_2.set_index("Name")["Status"].to_dict()
        # d2_keys = status_dict_2.keys()
    except Exception:
        print(
            "\n!!!!!!Please check whether the build numbers are correct,"
            "if any one of the build numbers is from custom/non-production"
            "jenkins job please add 'NP' before build number Example: 'python bdd_results_compare.py 4622 NP1961'\n\n"
        )
        quit()

    result_count_1 = dict(df_1["Status"].value_counts())
    result_count_2 = dict(df_2["Status"].value_counts())

    result_count_1["total"] = len(df_1)
    result_count_2["total"] = len(df_2)

    failed_in_2_passed_in_1 = []
    for key, value in status_dict_2.items():
        if value != "passed" and status_dict_1.get(key, "NA") == "passed":
            failed_in_2_passed_in_1.append(key)

    # To analyse and get more info
    """
    #from deepdiff import DeepDiff
    deep_diff = DeepDiff(status_dict_1,status_dict_2)
    run_only_in_1 = {
        'count': len(deep_diff['dictionary_item_removed']),
        'tests': deep_diff['dictionary_item_removed']
        }
    run_only_in_2 = {
        'count': len(deep_diff['dictionary_item_added']),
        'tests': deep_diff['dictionary_item_added']
        }
    """
    return [result_count_1, result_count_2, status_dict_1, status_dict_2, failed_in_2_passed_in_1]


def print_result_comparisions(results):
    result_count_1, result_count_2, status_dict_2, failed_in_2_passed_in_1 = (
        results[0],
        results[1],
        results[3],
        results[4],
    )
    pass_percentage_1 = float("{:.2f}".format((result_count_1["passed"] / result_count_1["total"]) * 100))
    pass_percentage_2 = float("{:.2f}".format((result_count_2["passed"] / result_count_2["total"]) * 100))
    message = "\n\nTest Results Summary:\n\n"
    results_rows = []
    results_rows.append(
        [
            "Baseline Run",
            result_count_1["passed"],
            result_count_1["failed"],
            result_count_1["broken"],
            result_count_1["total"],
            pass_percentage_1,
        ]
    )
    results_rows.append(
        [
            "Current Run",
            result_count_2["passed"],
            result_count_2["failed"],
            result_count_2["broken"],
            result_count_2["total"],
            pass_percentage_2,
        ]
    )
    results_rows.append(
        [
            "Diff",
            abs(result_count_2["passed"] - result_count_1["passed"]),
            abs(result_count_2["failed"] - result_count_1["failed"]),
            abs(result_count_2["broken"] - result_count_1["broken"]),
            abs(result_count_2["total"] - result_count_1["total"]),
        ]
    )

    results_column = ["Run", "Passed", "Failed", "Broken", "Total", "Pass %"]

    message += tabulate(results_rows, headers=results_column, tablefmt="grid")

    message += "\n\nBelow are the scenarios that passed in {} but not in {}, meaning increamentally failed/broken: ({})\n\n".format(
        "Baseline Run", "Current Run", len(failed_in_2_passed_in_1)
    )

    scenarios_rows = []
    for v in zip(*[failed_in_2_passed_in_1]):
        scenarios_rows.append([*v, status_dict_2[v[0]]])

    scenarios_column = ["Scenario Name", "Status"]

    message += tabulate(scenarios_rows, headers=scenarios_column, tablefmt="grid")
    print(message)

    # To create a text-image
    """
    #from PIL import Image, ImageDraw
    width = 700
    height = 1500

    img = Image.new('RGB', (width, height), color='white')

    imgDraw = ImageDraw.Draw(img)

    imgDraw.text((10, 10), message, fill=(0, 0, 0))

    img.save('result.png')
    """


def main(**kwargs):

    baseline_run_id, current_run_id = kwargs.get("baseline_run"), kwargs.get("current_run")

    # Get current and baseline url using bdd jenkins job build numbers, provided as input argument to the script
    url_list = get_urls(baseline_run_id, current_run_id)

    username = kwargs.get("username")
    password = kwargs.get("password")
    if not (username and password):
        print("\nEnter jenkins credentials:\n")
        username = input("Username:")
        password = getpass.getpass("Password for " + username + ":")
        if "@cisco.com" in username:
            username = username.split("@cisco.com")[0]

    # Download the both regression run results and create the diff
    results = get_results(url_list, baseline_run_id, current_run_id, username, password)

    # Print the comparison in readable table format
    print_result_comparisions(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--baseline_run", required=True)
    parser.add_argument("-c", "--current_run", required=True)
    parser.add_argument("-u", "--username")
    parser.add_argument("-p", "--password")
    args = parser.parse_args()
    kwargs = vars(args)
    main(**kwargs)
