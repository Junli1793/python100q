#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def compare_2_version(version1, version2):
    # Split the version
    version1_parts = list(map(int, version1.split(".")))
    version2_parts = list(map(int, version2.split(".")))

    # Compare
    for i in range(min(len(version1_parts), len(version2_parts))):
        if version1_parts[i] > version2_parts[i]:
            return True
        elif version1_parts[i] < version2_parts[i]:
            return False

    if len(version1_parts) > len(version2_parts):
        return True
    elif len(version1_parts) < len(version2_parts):
        return False
    else:
        return True


def compare_versions(*versions):
    version_list = list(versions)
    for i in range(len(version_list)):
        for j in range(i + 1, len(version_list)):
            if compare_2_version(version_list[i], version_list[j]):
                version_list[i], version_list[j] = version_list[j], version_list[i]

    return version_list

print(compare_versions("12.4.32", "15", "12.4"))
print(compare_versions("11.1", "11.1.0"))

