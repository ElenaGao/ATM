# 项目需求
    模拟实现一个ATM + 购物商城程序

    1. 额度 15000或自定义  --> 注册功能，给用户设置信用卡额度
    2. 实现购物商城，买东西加入 购物车，调用信用卡接口结账  --> 购物 支付功能
    3. 可以提现，手续费5%  --> 提现功能
        每月22号出账单，每月10号为还款日，过期未还，按欠款总额 万分之5 每日计息
    4. 支持多账户登录  --> 登录功能
    5. 支持账户间转账  --> 转账功能
    6. 记录每月日常消费流水  --> 记录流水功能
    7. 提供还款接口 --> 还款功能
    8. ATM记录操作日志  --> 记录日志功能
    9. 提供管理接口，包括添加账户、用户额度，冻结账户等。。。--> 管理员功能
    10. 用户认证用装饰器  --> 登录装饰器
    
    
 # 需求分析
    - 用户视图层
        1. 注册功能
        2. 登录功能
        3. 查看余额
        4. 提现功能
        5. 还款功能
        6. 转账功能
        7. 查看流水功能
        8. 购物功能
        9. 查看购物车
        10. 管理员功能
        
    - 逻辑接口层
        
    