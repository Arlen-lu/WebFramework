'''投标数据'''
invest_success = [{'invest_ammount':1000,'msg':'投标成功！'},]
invest_wrong = [
                {'invest_ammount':0,'msg':'请正确填写投标金额'},
                {'invest_ammount':110,'msg':'投标金额必须为100的倍数'},
                # {'invest_ammount':1000000,'msg':'购买标的金额不能大于标总金额'},
                {'invest_ammount':999999999999990,'msg':'投标金额大于可用金额'}
                ]
invest_not_multiple_of_10 = [{'invest_ammount':15,'msg':'请输入10的整数倍'},]

# ---
# invest_datas: 
#   invest_success: 
#     - 
#       invest_ammount: 100
#       msg: '投标成功'
#   invest_wrong: 
#     -
#       invest_ammount: 0
#       msg: '请正确填写投标金额'
#     - 
#       invest_ammount: 110
#       msg: '投标金额必须为100的倍数'
#     - 
#       invest_ammount: 550000
#       msg: '购买标的金额不能大于标总金额'
#     - 
#       invest_ammount: 999999999999990
#       msg: '投标金额大于可用金额'
#   invest_not_multiple_of_10: 
#     - 
#       invest_ammount: 15
#       msg: '请输入10的整数倍'