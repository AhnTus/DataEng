# with open('filename.txt', 'r') as f:
#     with open('foldername.txt', 'w') as f2:
#         lines = f.readlines()
#         foldername = ['']
#         for line in lines:
#             if line == 'No data found!\n':
#                 foldername.append('\n')
#                 f2.writelines('\n')
#             elif line[-5:-1] == '.zip':
#                 foldername.append(line[-13:-5] + '\n')
#                 f2.writelines(line[-13:-9] + '-' + line[-9:-7] + '-' + line[-7:-5] + '\n')
#             elif line[-5:-1] == '.tic':
#                 foldername.append(line[-17:-9] + '\n')
#                 f2.writelines(line[-17:-13] + '-' + line[-13:-11] + '-' + line[-11:-9] + '\n')
#             elif line[-4:-1] == '.gz':
#                 foldername.append(line[-12:-4] + '\n')
#                 f2.writelines(line[-12:-8] + '-' + line[-8:-6] + '-' + line[-6:-4] + '\n')
#             elif line[-5:-1] == '.txt':
#                 foldername.append(line[-17:-9] + '\n')
#                 f2.writelines(line[-17:-13] + '-' + line[-13:-11] + '-' + line[-11:-9] + '\n')
#
# import json
# with open('foldername.txt','r') as f:
#     lines = f.readlines()
#     dict = {}
#     with open('dateHistory.json','w') as f2:
#         for i in range(len(lines)):
#             if lines[i] != '\n':
#                 dict[lines[i][:-1]] = i + 1
#         json.dump(dict,f2)

# import  requests
# for i in range(1,5382):
#     try:
#         cvDate = str(i)
#         URL = "https://links.sgx.com/1.0.0/derivatives-historical/" + cvDate + "/TC.txt"
#         response = requests.get(URL)
#         header = response.headers.get('Content-Disposition')
#         open("filename2", "a").write(header + "\n")
#     except:
#         open("filename2", "a").write("No data found!" + "\n")

import datetime

print(datetime.datetime.today().weekday())