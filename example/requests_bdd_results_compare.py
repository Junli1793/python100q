import sys
import getpass
import requests
import pandas as pd

# from deepdiff import DeepDiff
# from PIL import Image, ImageDraw

baseline_run, current_run = sys.argv[1], sys.argv[2]

production_job = 'assurance-it-regression-bdd-on-prem-in-docker/'
non_production_job = 'assurance-it-regression-bdd-on-prem-in-docker-non-production/'

if 'NP' in baseline_run:
    baseline_run = str(baseline_run).split('NP')[1]
    baseline_run_url = 'https://engci-private-sjc.cisco.com/jenkins/thunderbolt/job/' + non_production_job + baseline_run + '/allure/data/suites.csv'
else:
    baseline_run_url = 'https://engci-private-sjc.cisco.com/jenkins/thunderbolt/job/' + production_job + str(
        baseline_run) + '/allure/data/suites.csv'

if 'NP' in current_run:
    current_run = str(current_run).split('NP')[1]
    current_run_url = 'https://engci-private-sjc.cisco.com/jenkins/thunderbolt/job/' + non_production_job + current_run + '/allure/data/suites.csv'
else:
    current_run_url = 'https://engci-private-sjc.cisco.com/jenkins/thunderbolt/job/' + production_job + str(
        current_run) + '/allure/data/suites.csv'

user = input("Username:")
passwd = getpass.getpass("Password for " + user + ":")
if '@cisco.com' in user:
    user = user.split('@cisco.com')[0]

baseline_run_response = requests.get(baseline_run_url, auth=(user, passwd))
current_run_response = requests.get(current_run_url, auth=(user, passwd))

baseline_run_file = 'suites_' + baseline_run + '.csv'
current_run_file = 'suites_' + current_run + '.csv'

with open(baseline_run_file, 'wb') as out:
    for bits in baseline_run_response.iter_content():
        out.write(bits)

with open(current_run_file, 'wb') as out:
    for bits in current_run_response.iter_content():
        out.write(bits)

df_1 = pd.read_csv(baseline_run_file, usecols=['Name', 'Status'])
status_dict_1 = df_1.set_index('Name')['Status'].to_dict()
d1_keys = status_dict_1.keys()

df_2 = pd.read_csv(current_run_file, usecols=['Name', 'Status'])
status_dict_2 = df_2.set_index('Name')['Status'].to_dict()
d2_keys = status_dict_2.keys()

result_count_1 = dict(df_1['Status'].value_counts())
result_count_2 = dict(df_2['Status'].value_counts())

result_count_1['total'] = len(df_1)
result_count_2['total'] = len(df_2)

failed_in_2_passed_in_1 = []
for key, value in status_dict_2.items():
    if value != 'passed' and status_dict_1.get(key, 'NA') == 'passed':
        failed_in_2_passed_in_1.append(key)
'''
deep_diff = DeepDiff(status_dict_1,status_dict_2)
run_only_in_1 = {
    'count': len(deep_diff['dictionary_item_removed']), 
    'tests': deep_diff['dictionary_item_removed']
    }
run_only_in_2 = {
    'count': len(deep_diff['dictionary_item_added']), 
    'tests': deep_diff['dictionary_item_added']
    }
'''

pass_percentage_1 = float("{:.2f}".format((result_count_1['passed'] / result_count_1['total']) * 100))
pass_percentage_2 = float("{:.2f}".format((result_count_2['passed'] / result_count_2['total']) * 100))

'''
message += "\nResults:"
message += "\n________\n"
message += "\n{:<15} {:<10} {:<10} {:<10} {:<10} {:<10}".format('Run', 'Passed', 'Failed', 'Broken', 'Total', 'Pass %')
message += "\n___             ______     ______     ______     ______     ______\n"
message += "\n{:<15} {:<10} {:<10} {:<10} {:<10} {:<10}".format('Baseline', result_count_1['passed'], result_count_1['failed'], result_count_1['broken'], result_count_1['total'], pass_percentage_1)
message += "\n{:<15} {:<10} {:<10} {:<10} {:<10} {:<10}".format('Current Run', result_count_2['passed'], result_count_2['failed'], result_count_2['broken'], result_count_2['total'], pass_percentage_2)
message += "\n{:<15} {:<10} {:<10} {:<10} {:<10}\n".format('Diff', abs(result_count_2['passed']-result_count_1['passed']), abs(result_count_2['failed']-result_count_1['failed']), abs(result_count_2['broken']-result_count_1['broken']), abs(result_count_2['total']-result_count_1['total']))


message += "\nPassed in {} but not in {}: {}".format('Baseline', 'Current run', len(failed_in_2_passed_in_1))
message += "\n_____________________________________________\n"
message += "\n{:<10} {:<100}".format('Status','Scenario Name')
message += "\n______     _____________\n"
for v in zip(*[failed_in_2_passed_in_1]):
    message += "\n{:<10} {:<100}".format(status_dict_2[v[0]],*v)
'''

from tabulate import tabulate

message = "\n\nTest Results Summary:\n\n"
results_rows = []
results_rows.append(
    ['Baseline({})'.format(baseline_run), result_count_1['passed'], result_count_1['failed'], result_count_1['broken'],
     result_count_1['total'], pass_percentage_1])
results_rows.append(['Current Run({})'.format(current_run), result_count_2['passed'], result_count_2['failed'],
                     result_count_2['broken'], result_count_2['total'], pass_percentage_2])
results_rows.append(['Diff', abs(result_count_2['passed'] - result_count_1['passed']),
                     abs(result_count_2['failed'] - result_count_1['failed']),
                     abs(result_count_2['broken'] - result_count_1['broken']),
                     abs(result_count_2['total'] - result_count_1['total'])])

results_column = ['Run', 'Passed', 'Failed', 'Broken', 'Total', 'Pass %']

message += tabulate(results_rows, headers=results_column, tablefmt="grid")

message += "\n\nPassed in {} but not in {}: {}\n\n".format('Baseline({})'.format(baseline_run),
                                                           'Current run({})'.format(current_run),
                                                           len(failed_in_2_passed_in_1))

scenarios_rows = []
for v in zip(*[failed_in_2_passed_in_1]):
    scenarios_rows.append([*v, status_dict_2[v[0]]])

scenarios_column = ['Scenario Name', 'Status']

message += tabulate(scenarios_rows, headers=scenarios_column, tablefmt="grid")
print(message)

'''
width = 700
height = 1500

img = Image.new('RGB', (width, height), color='white')

imgDraw = ImageDraw.Draw(img)

imgDraw.text((10, 10), message, fill=(0, 0, 0))

img.save('result.png')
'''
