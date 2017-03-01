# File-Operation
copy a tree to another by Python<br>
###文件备份<br>
通过比对两目录下所有文件的MD5值，判断source文件夹下是否新增文件或文件被修改。
将新文件及修改过的文件通过增量更新的方法拷贝至destination文件夹。

<br>对于原来存在但被修改过的文件，在拷贝时，文件名头部追加拷贝时间，以免destination下文件被覆盖，实现多版本控制。
