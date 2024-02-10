import subprocess
import json



# result = subprocess.run(['ps',  'aux', '|','awk', '{print $2}'])


# cmd = "ps aux | awk '{print $2}'"
# ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
# output = ps.communicate()[0]
# print(output)

# print(result)

# with open ('output.json', 'w') as file:
#     json.dump(result, file)
    
    
    


ps = subprocess.Popen(('ps', 'ps aux '), stdout=subprocess.PIPE)
output = subprocess.check_output(('awk', "'{print $2}'"), stdin=ps.stdout)
ps.wait()