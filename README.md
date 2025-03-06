# LLM-For-Math

# 简介
    A mathematical problem solver based on the Multi-Modal Large Model from Zero One All Things.

# 环境依赖
    1) Request python >= 3.8 to run OpenAI pkg.
 
# 目录结构描述
    ├── main.py             // main work in python
    
    ├── img_dir             // 测试图片集
    
    │   ├── Calculus.jpg

    │   ├── Calculus_2.jpg

    │   ├── Limit.jpg

    │   ...

    └── ReadMe.md           // 说明文档 

# 使用说明
    1) Run main.py after the needed pkgs are all installed.
    
    2) To have a better result, run the LLM for twice. The first running for thinking, while another for analysis the result from the last thinking, and give the final result.
    
    3) In the future version, we' re gonna(if time permits) add Multi-process mode to share results with other processes.

# 版本内容更新
###### v0:
    1. 实现“零一万物”多模态大模型的调用
###### v1:
    1. 基于 ROS::CV_Bridge 实现进程间图像共享；
    2. 基于 ROS::Topic 实现进程间数据共享；
