import pymysql
import time

'''sql工具类'''

# def get_conn():
#     conn = pymysql.connect(host="localhost", user="root", password="root",
#                            database="five_project", port=3306, unix_socket=None,
#                            charset='utf8')
#
#     cursor = conn.cursor()  # 游标
#     return conn, cursor

def get_conn():
    conn = pymysql.connect(host="193.112.191.40", user="root", password="971027",
                           database="five_project", port=3306, unix_socket=None,
                           charset='utf8')

    cursor = conn.cursor()  # 游标
    return conn, cursor

# 关闭数据库连接
def close_conn(conn, cursor):
    cursor.close() #没必要判断，直接关闭
    conn.close()

# 查找操作
def query(sql, *args):
    # 创建数据库连接
    conn, cursor = get_conn()

    cursor.execute(sql, *args)
    result = cursor.fetchall()

    return result
'''
# 删除操作
def exeDelete(sql,delete_id):
    conn, cursor = get_conn()
    sta=0
    sta+=cursor.execute("delete from students where Id=%d"%(int(delete_id)))
    conn.commit()
    return (sta)
'''

# 累计top5
# def query_top5():
#     query_sql = '  SELECT  area,housetot  FROM test order by housetot desc limit 5'
#     result = query(query_sql)
#     return result
#
# # def query_pop():
# #     query_sql = ' SELECT  area,peopletot  FROM test'
# #     result = query(query_sql)
# #     return result
#
# def query_min():
#     query_sql = ' SELECT  years,menggu,hui,zang  FROM national_population where years!= 0 '
#     result = query(query_sql)
#     return result
#
# def query_edu():
#     query_sql = ' SELECT  Noschool,collage  FROM education  where Noschool!= "6-9岁" '
#     result = query(query_sql)
#     return result
#
# def query_map():
#     query_sql = ' SELECT  name,value  FROM total '
#     result = query(query_sql)
#     return result
#
# def query_cloud():
#     query_sql = ' SELECT  name,value  FROM total'
#     result = query(query_sql)
#     return result
#分页


#数据展示部分###################################################################################################################################
#学科竞赛
def contest_show(page_num, page_size):
    index_page=(page_num-1)*page_size
   # page_size=10
    query_sql = ' SELECT * from contest_show LIMIT {},{}'.format(
        index_page,page_size)
    result = query(query_sql)
    count_sql='select count(*) as count from contest_show'
    count = query(count_sql)[0][0]
    return result,count

#专利申请
def patent_show(page_num,page_size):
    index_page=(page_num-1)*page_size
   # page_size=10
    query_sql = ' SELECT * from patent_show LIMIT {},{}'.format(
        index_page,page_size)
    result = query(query_sql)
    count_sql='select count(*) as count from patent_show'
    count = query(count_sql)[0][0]
    return result,count

#学术论文
def paper_show(page_num,page_size):
    index_page=(page_num-1)*page_size
   # page_size=10
    query_sql = ' SELECT * from paper_show LIMIT {},{}'.format(
        index_page,page_size)
    result = query(query_sql)
    count_sql='select count(*) as count from paper_show'
    count = query(count_sql)[0][0]
    return result,count

#课题申报
def issue_show(page_num,page_size):
    index_page=(page_num-1)*page_size
   # page_size=10
    query_sql = ' SELECT * from issue_show LIMIT {},{}'.format(
        index_page,page_size)
    result = query(query_sql)
    count_sql='select count(*) as count from issue_show'
    count = query(count_sql)[0][0]
    return result,count

#创业项目
def business_show(page_num,page_size):
    index_page=(page_num-1)*page_size
   # page_size=10
    query_sql = ' SELECT * from business_show LIMIT {},{}'.format(
        index_page,page_size)
    result = query(query_sql)
    count_sql='select count(*) as count from business_show'
    count = query(count_sql)[0][0]
    return result,count

#老师列表_搜索
def teacher_show():
    search_sql = ' select * from teacher '
    result = query(search_sql)
    return result

#竞赛列表_搜索
def contestList():
    search_sql = ' select * from contest '
    result = query(search_sql)
    return result

#===================================查询=============================================

#学科竞赛_搜索
def contest_search(search_string):
    search_sql = ' select * from contest_show pat where pat.search like "%{}%"'.format(
        search_string)
    result = query(search_sql)
    return result

#专利申请_搜索
def patent_search(search_string):
    search_sql = ' select * from patent_show pat where pat.search like "%{}%"'.format(
        search_string)
    result = query(search_sql)
    return result

#学术论文_搜索
def paper_search(search_string):
    search_sql = ' select * from paper_show pat where pat.search like "%{}%"'.format(
        search_string)
    result = query(search_sql)
    return result

#课题申报_搜索
def issue_search(search_string):
    search_sql = ' select * from issue_show pat where pat.search like "%{}%"'.format(
        search_string)
    result = query(search_sql)
    return result

#创业项目_搜索
def business_search(search_string):
    search_sql = ' select * from business_show pat where pat.search like "%{}%"'.format(
        search_string)
    result = query(search_sql)
    return result

#===================================添加=============================================

#学科竞赛_添加
def contest_insert(year,name_contest,host_contest,classes,level_contest,obtain_contest,time1,production,teacher,leader,leader_major,team,search):
    # 注意:这里的time字段改为time1,因为调用time.py包时编译器分不清time是变量名还是time包
    conn, cursor = get_conn()
    sta=0
    sta+=cursor.execute(" INSERT INTO contest_show (year,name_contest,host_contest,classes,level_contest,obtain_contest,time,production,teacher,leader,leader_major,team,search) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(
        year,name_contest,host_contest,classes,level_contest,obtain_contest,time1,production,teacher,leader,leader_major,team,search))
    text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" ,添加contest表中name="+name_contest+"条目,"+" 是否成功:"+str(sta)
    cursor.execute("INSERT INTO action_log (action,text) VALUES ('insert','%s')"%(text))
    conn.commit() #提交到数据库
    return (sta)

#===================================修改=============================================

#学科竞赛_修改
def contest_update(id,year,name_contest,host_contest,classes,level_contest,obtain_contest,time1,production,teacher,leader,leader_major,team,prove,search):
    # 注意:这里的time字段改为time1,因为调用time.py包时编译器分不清time是变量名还是time包
    conn, cursor = get_conn()
    sta=0
    sta+=cursor.execute(" UPDATE contest_show SET year='%s',name_contest='%s',host_contest='%s',classes='%s',level_contest='%s',obtain_contest='%s',time='%s',production='%s',teacher='%s',leader='%s',leader_major='%s',team='%s',prove='%s',search='%s' WHERE id='%s'"%(
        year,name_contest,host_contest,classes,level_contest,obtain_contest,time1,production,teacher,leader,leader_major,team,prove,search,id))
    text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" ,修改contest表中name="+name_contest+"条目,"+" 是否成功:"+str(sta)
    cursor.execute("INSERT INTO action_log (action,text) VALUES ('update','%s')"%(text))
    conn.commit() #提交到数据库
    return (sta)

#===================================删除=============================================

#学科竞赛_删除
def contest_delete(delete_id):
    conn, cursor = get_conn()
    sta=0
    sta+=cursor.execute("delete from contest_show where Id=%d"%(int(delete_id)))
    # 进行日志备份,时间+操作+具体id
    text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" ,删除contest表中id="+delete_id+"条目,"+" 是否成功:"+str(sta)
    cursor.execute("INSERT INTO action_log (action,text) VALUES ('delete','%s')"%(text))
    conn.commit() #提交到数据库
    return (sta)

#专利申请_删除
def patent_delete(delete_id):
    conn, cursor = get_conn()
    sta=0
    sta+=cursor.execute("delete from patent_show where Id=%d"%(int(delete_id)))
    # 进行日志备份,时间+操作+具体id
    text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" ,删除patent表中id="+delete_id+"条目,"+" 是否成功:"+str(sta)
    cursor.execute("INSERT INTO action_log (action,text) VALUES ('delete','%s')"%(text))
    conn.commit() #提交到数据库
    return (sta)

#学术论文_删除
def paper_delete(delete_id):
    conn, cursor = get_conn()
    sta=0
    sta+=cursor.execute("delete from paper_show where Id=%d"%(int(delete_id)))
    # 进行日志备份,时间+操作+具体id
    text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" ,删除paper表中id="+delete_id+"条目,"+" 是否成功:"+str(sta)
    cursor.execute("INSERT INTO action_log (action,text) VALUES ('delete','%s')"%(text))
    conn.commit() #提交到数据库
    return (sta)

#课题申报_删除
def issue_delete(delete_id):
    conn, cursor = get_conn()
    sta=0
    sta+=cursor.execute("delete from issue_show where Id=%d"%(int(delete_id)))
    # 进行日志备份,时间+操作+具体id
    text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" ,删除issue表中id="+delete_id+"条目,"+" 是否成功:"+str(sta)
    cursor.execute("INSERT INTO action_log (action,text) VALUES ('delete','%s')"%(text))
    conn.commit() #提交到数据库
    return (sta)
#创业项目_删除
def business_delete(delete_id):
    conn, cursor = get_conn()
    sta=0
    sta+=cursor.execute("delete from business_show where Id=%d"%(int(delete_id)))
    # 进行日志备份,时间+操作+具体id
    text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" ,删除business表中id="+delete_id+"条目,"+" 是否成功:"+str(sta)
    cursor.execute("INSERT INTO action_log (action,text) VALUES ('delete','%s')"%(text))
    conn.commit() #提交到数据库
    return (sta)
#===================================登录检查=============================================
def loginCheck(username,password):
    query_sql = "select count(*) from user u where u.username = '{}' and u.password = '{}'".format(
        username,password)
    result = query(query_sql)
    return result

#===================================日志操作=============================================
#保存日志
def saveLog(action,text):
    search_sql = " INSERT INTO action_log (action,text) VALUES ('{}','{}')".format(
        action,text)
    result = query(search_sql)
    print(result)
    return result

def searchLog(action_string):
    search_sql = ' select * from action_log where action like "%{}%"'.format(
        action_string)
    result = query(search_sql)
    print(result)
    return result
'''
#专利申请_修改
def patent_update(a,b,c,):
    search_sql = ' update patent_show 
    set year="{}", name="{}", number="{}", type="{}", time="{}", people="{}", major="{}", prove="{}" 
    where id = "2"'.format(
        search_string)
    result = query(search_sql)
    print(result)
    return result
'''