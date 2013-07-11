![logo](https://raw.github.com/alibaba/oceanbase/oceanbase_0.3/doc/%E5%9B%BE%E7%89%87%E5%A4%B9/logo.jpg)
<font size=5><b>[English Version](https://github.com/alibaba/oceanbase/wiki/Oceanbase)</b></font>

OceanBase是[阿里巴巴集团](http://page.china.alibaba.com/shtml/about/ali_group1.shtml)自主研发的可扩展的关系型数据库，OceanBase实现了跨行跨表的事务，支持数千亿条记录、数百TB数据上的SQL操作，截止到2012年8月为止，OceanBase数据库支持了阿里巴巴集团下多个重要业务的数据存储，支持业务包括收藏夹、直通车报表、天猫评价等，截止2013年4月份，OceanBase线上业务的数据量已经超过一千亿条。

从模块划分的角度看，OceanBase可以划分为四个模块：主控服务器RootServer、更新服务器UpdateServer、基准数据服务器ChunkServer以及合并服务器MergeServer。OceanBase系统内部按照时间线将数据划分为基准数据和增量数据，基准数据是只读的，所有的修改更新到增量数据中，系统内部通过合并操作定期将增量数据融合到基准数据中。

<h1>1 最新动态</h1>
<font color=“#0000E3”><b>2013/06/19，合并最新的bugfix和特性到0.41分支上：</b> </font>

【重要】RootServer: Chunk Server在合并失败后，如果发现其他两个副本已经成功合并，会本地直接删除失败的副本，以前的版本RootServer并没有处理主动删除replica的情况;

SQL: ob_tablet_get.cpp的reset方法没有实现完全，这个bug会导致select * from t1 as z where k1 = 1不断执行时失败；

SQL：group_min_max.test执行cs出core，原因是ob_row_store重用时有错，造成sort操作符访问到额外数据，致使比较类型出错，std::sort会core掉; 

[查看发布说明](https://github.com/alibaba/oceanbase/wiki/OceanBase-0.4.1-1209%E5%8F%91%E5%B8%83%E8%AF%B4%E6%98%8E)

<h1>2 发行日志</h1>
- <font color=“#0000E3”><b>2013/04/28，整理提交了V0.4.1代码和相关技术文档。</b> </font>
- 2013/03/04，整理提交了V0.3.1代码和相关技术文档。

<h1>3 版本特性</h1>
- 使用libeasy网络框架代替了原来的tbnet，实现更高的网络处理性能
- 全面支持mysql协议
- 支持SQL的客户端库
- 全面支持SQL
- 易用性改进

[详细列表](https://github.com/alibaba/oceanbase/wiki/OceanBase-0.4-%E7%89%88%E6%9C%AC%E7%89%B9%E6%80%A7) 

<h1>4 文档导读</h1>
<table width="100%"  border="1" frame="all" rules="all">
  <tr>
    <td width=7% bgcolor="B0B0B0"><b>序号</b></div></td>
    <td width=33% bgcolor="B0B0B0"><b>文档名称</b></td>
    <td width=60% bgcolor="B0B0B0"><b>使用说明</b></td>
  </tr>
  <tr>
    <td width="7%"><div align="center">1</div></td>
    <td width="33%"><a href="https://github.com/alibaba/oceanbase/wiki/OceanBase%E6%9E%B6%E6%9E%84%E4%BB%8B%E7%BB%8D" target="_blank">《OceanBase架构》</a></td>
    <td width="60%">该文档主要介绍OceanBase数据库的功能、架构、特点和工作模式等信息。</td>
  </tr>
  <tr>
    <td width="7%"><div align="center">2</div></td>
    <td width="33%"><a href="/alibaba/oceanbase/wiki/OceanBase-0.4-%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97" target="_blank">《OceanBase 0.4 安装指南》</a></td>
    <td width="60%">该文档主要介绍OceanBase数据库的安装过程。</td>
  </tr>
  <tr>
    <td width="7%"><div align="center">3</div></td>
    <td width="33%"><a href="/alibaba/oceanbase/wiki/OceanBase%E5%AE%A2%E6%88%B7%E7%AB%AF-%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97" target="_blank">《OceanBase 客户端 用户指南》</a></td>
    <td width="60%">该文档主要介绍OceanBase数据库的Java客户端和C客户端的使用方法。</td>
  </tr>
  <tr>
    <td width="7%"><div align="center">4</div></td>
    <td width="33%"><a href="https://github.com/alibaba/oceanbase/wiki/OceanBase-SQL-%E5%8F%82%E8%80%83%E6%8C%87%E5%8D%97" target="_blank">《OceanBase SQL 参考指南》</a></td>
    <td width="60%">该文档主要介绍OceanBase数据库支持的SQL语言、语法规则和使用方法等。</td>
  </tr>
</table>

<h1>5 其他资源列表</h1>
* [OceanBase SQL 用户参考手册](https://github.com/alibaba/oceanbase/wiki/OceanBase-SQL-%E7%94%A8%E6%88%B7%E5%8F%82%E8%80%83%E6%89%8B%E5%86%8C)
* [OceanBase SQL管理员手册](https://github.com/alibaba/oceanbase/wiki/OceanBase-SQL%E7%AE%A1%E7%90%86%E5%91%98%E6%89%8B%E5%86%8C)
* [ChunkServer设计文档](https://github.com/alibaba/oceanbase/tree/oceanbase_0.4/doc/chunkserver%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3)
* [mergeServer设计文档](https://github.com/alibaba/oceanbase/tree/oceanbase_0.4/doc/mergeserver%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3)
* [rootServer设计文档](https://github.com/alibaba/oceanbase/tree/oceanbase_0.4/doc/rootserver%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3)
* [updateServer设计文档](https://github.com/alibaba/oceanbase/tree/oceanbase_0.4/doc/updateserver%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3)
* [运维文档](https://github.com/alibaba/oceanbase/tree/oceanbase_0.4/doc/%E4%BD%BF%E7%94%A8%E8%BF%90%E7%BB%B4)
* [Project Plan](https://github.com/alibaba/oceanbase/wiki/Project-Plan) 

<h1>6 联系我们</h1>
 <p align="left">如果您有任何疑问或是想了解OceanBase的最新开源动态消息，请联系我们：</p>
  <p align="left"><b>支付宝（中国）网络技术有限公司·OceanBase团队</b></p>
  <p align="left">地址：杭州市万塘路18号黄龙时代广场B座</p>
  <p align="left">邮编：310099</p>
  <p align="left">邮箱： <a href="mailto:rongxuan.lc@alipay.com">rongxuan.lc@alipay.com</a></p>
  <p align="left"> 新浪微博：<a href="http://weibo.com/u/2356115944">http://weibo.com/u/2356115944</a></p>
  <p align="left">技术交流群（阿里旺旺）：853923637</p>
