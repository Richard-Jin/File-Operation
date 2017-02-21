# D:\Python\Python35\python
# -*- coding:utf-8 -*-


import logging,time,shutil,os,hashlib

f1=r'X:\sect1\2 试验数据\RAC\17S\NS'
f2=r'D:\E Virtual\NS Local\~试验数据备份'
log_f_p=r'D:\E Virtual\NS Local\~试验数据备份\fileCompare.log'
exe_time=time.strftime('%Y%m%d%H%M%S')

logging.basicConfig(filename=log_f_p,level=logging.INFO,format='%(asctime)s %(message)s')

def md5_calc(file):         #计算文件的MD5
    md5_value=hashlib.md5()
    with open(file,'rb') as file_b:
        while True:
            data_flow=file_b.read(8096)
            if not data_flow:
                break
            md5_value.update(data_flow)
    file_b.close()
    return md5_value.hexdigest()

def dir_md5_dict(dir_path):  #计算目录下所有文件的MD5值，以MD5值为key,path为Value创建词典
    dir_walk=os.walk(dir_path)
    md5_dict={}
    for walk_item in dir_walk:
        a=walk_item[0]
        b=walk_item[1]
        c=walk_item[2]
        for file_item in c:
            file_path=a+'\\'+file_item
            # print(file_path)
            if os.path.isfile(file_path):
                file_md5=md5_calc(file_path)
                # print(file_md5)
                md5_dict[file_md5]=file_path
            # else:
                # print('non md5')
    return md5_dict

src_md5_dict=dir_md5_dict(f1)   #源文件所有MD5字典
dst_md5_dict=dir_md5_dict(f2)   #目标目录下所有文件MD5字典

for key in src_md5_dict.keys():
    if key in dst_md5_dict.keys():
        exist_f_p=src_md5_dict[key]
        # exist_f_p=exist_f_p.encode('gbk')
        # logging.info(exist_f_p)
        # exist_f_p=exist_f_p[24:]    # NS\COMP\KNB065FYJMC(铝线化) KNB092FFDMC(VE) 压缩机一次设试手配需求.xlsx
        # print('已备份:',exist_f_p)
    else:
        unexist_f_p=src_md5_dict[key]
        src=unexist_f_p      #X:\sect1\2 试验数据\RAC\17S\NS\test.txt
        relative_p=unexist_f_p[27:]    #VE项目\STOP_V 调查\stop_v図面\SU50V237.tif
        i=relative_p.rfind('\\')

        #判断是否目标文件夹根目录
        if not i==-1:
            relative_dir = relative_p[:relative_p.rfind('\\')]  # VE项目\STOP_V 调查\stop_v図面
        else:
            relative_dir=''

        logging.debug('relative_dir:   '+relative_dir)
        dst_dir=f2+'\\'+relative_dir        #D:\E Virtual\NS Local\~试验数据备份\VE项目\STOP_V 调查\stop_v図面
        logging.debug('innitial:'+dst_dir)
        dst=f2+'\\'+relative_p     #D:\E Virtual\NS Local\~试验数据备份\VE项目\STOP_V 调查\stop_v図面\SU50V237.tif

        if os.path.exists(dst):
            dst = dst[:dst.rfind('\\') + 1] + exe_time + '__' + dst[dst.rfind('\\') + 1:]
            logging.debug('进入判断' + dst)

        if os.path.exists(dst_dir):
            pass
        else:
            os.makedirs(dst_dir)
            logging.debug('makedir:'+dst_dir)

        shutil.copy2(src, dst)
        logging.info('      This time back up:      '+dst)

logging.info('__________________Back up over_________________'+'\n'+'\n'+'\n'+'\n')    #运行结束后在日志末尾加空行


