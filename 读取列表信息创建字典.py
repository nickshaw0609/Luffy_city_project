"""
原文件形式：
Enclosure Device ID: 32
Slot Number: 1
Drive's postion: DiskGroup: 0, Span: 0, Arm: 0
Enclosure position: 0
Device Id: 0
WWN: 5000C5007272C288
Sequence Number: 2
Media Error Count: 0
Other Error Count: 0
Predictive Failure Count: 0
Last Predictive Failure Event Seq Number: 0
PD Type: SAS
Raw Size: 279.396 GB
Non Coerced Size: 278.896 GB [0x22dcb25c Sectors]
Coerced Size: 278.875 GB [0x22dc0000 Sectors]
Firmware state: Online, Spun Up
Device Firmware Level: LS08
Shield Counter: 0
Successful diagnostics completion on :  N/A
SAS Address(0): 0x5000c5007272c289
SAS Address(1): 0x0
Connected Port Number: 0(path0)
Inquiry Data: SEAGATE ST300MM0006     LS08S0K2B5NV
FDE Enable: Disable
Secured: Unsecured
Locked: Unlocked
Needs EKM Attention: No
Foreign State: None

目标文件格式：
info = {
    "slot":"1",
    "capacity":"279.396 GB",
    "model":"SEAGATE ST300MM0006     LS08S0K2B5NV",
    "pd_type":"SAS"
}
"""

list = []
info = {}
target = ["Slot Number", "Raw Size", "Inquiry Data", "PD Type"]
res = ["slot", "capacity", "model", "pd_type"]  # res中的元素与target中一一对应
f = open("计算机信息.txt", encoding='utf-8')

for line in f:
    line = line.strip()
    list.append(line)

for each in list:
    target_name = each.split(":")[0]
    value = each.split(":")[1]
    if target_name in target:
        index = target.index(f"{target_name}")
        info[res[index]] = value

print(info)
