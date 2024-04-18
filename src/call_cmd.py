from re import sub
import subprocess
 
""" 命令行调用练习 """

# 调用命令行命令并获取输出
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
 
# 打印输出
print("stdout:", result.stdout)
print("stderr:", result.stderr)

# 不输出结果的调用
# 0正确 2异常
exit_code = subprocess.call(['ls','-l'])
print("exit code:",exit_code)