---
title: 《泰坦陨落2》动态皮肤（VTF）MOD制作教程
date: 2022-02-12 19:56:20
cover: https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/Snipaste_2022-03-16_19-14-25.jpg
tags:
 - 教程
 - 游戏
---
# 动态皮肤（VTF）MOD制作

<span style="color:rgb(131, 131, 131);">文档作者：HK560</span>

::: warning
注意此文档为旧文档，部分内容可能过时，但仍然具有参考价值
:::

## 前言
泰坦陨落2是由重生娱乐制作组开发一款快节奏FPS游戏，游戏由其畅快的高机动性枪战体验和独有的泰坦机甲而广受玩家好评。

本文是一篇关于如何为泰坦陨落2制作动态武器皮肤的教程。教程内容全部由本人HK560编写，感谢各位热爱泰坦陨落的玩家支持。

本教程为武器动态皮肤制作教程，其他泰坦皮肤或铁驭皮肤可参考本教程和其他文档进行类推，无论是是否动态静态的。

注意：泰坦陨落2皮肤制作有两种方式：一种是VTF方式，一种是DDS方式

简单描述差异: VTF方式能实现动态效果，可以打包为北极星MOD方便北极星启用禁用，缺点是**无法使用法线贴图AO贴图等**只能使用基础颜色贴图。而DDS方式只能是静态贴图，但是能够使用游戏所支持的法线贴图AO贴图发光贴图等，能再现游戏内贴图效果。两种方式打包制作复杂度类似。

**本文教程是动态皮肤教程，所以是VTF方式制作皮肤。**

**转载请标明原作者和原文章地址**

## 制作动态皮肤的大体流程


流程简述：
1. 获取武器模型文件
2. 获取武器模型对应贴图文件
3. 处理模型文件
4. 根据获得到的资源文件进行基础皮肤制作
5. 将基础皮肤处理为动态皮肤
6. 压缩动态皮肤文件
7. 打包导入皮肤文件
   
**动态皮肤原理：动态皮肤的贴图是由一帧帧的静态贴图组合而成，当这些贴图帧按顺序播放时候便形成了动画动态的贴图**

根据原理我们需要提前构思好皮肤如何制作

## 需要的工具软件和文档

### 用于解包打包获取资源文件的工具
- **Titanfall VPK Tool**
- **Legion v2.13**
- **RSPNVPK**
  
以上工具可以在我个人资源站获取：[链接](https://onedrive.elbadaernu.com/TTF2mods/Tools)

>其中Titanfall VPK Tool可能会误报毒

### 用于处理模型制作动态皮肤的软件
并不是都需要，看你做皮肤用到什么
- Blender （处理模型
- Adobe Substance 3D Painter （模型绘制贴图
- Adobe Photoshop （处理动态贴图
- Adobe Premiere Pro （处理动态贴图
- Caesium （压缩贴图文件
- Hex Editor Neo (编辑文件十六进制
  
### 帮助文档站点
- [NoSkill](https://noskill.gitbook.io/titanfall2/) 

## 教程主体
### 获得武器模型文件
既然要为武器制作皮肤，那么我们首先需要取得武器模型文件，有了模型我们才方便绘制皮肤

大部分的武器模型文件储存在这两个文件中,这两个文件是一对的
- `\Titanfall2\vpk\client_mp_common.bsp.pak000_000.vpk`
- `\Titanfall2\vpk\englishclient_mp_common.bsp.pak000_dir.vpk`

当然这个vpk文件夹下还有许多其他资源文件，详细参考Noskill里的文档

那么我们要怎么打开这两个文件呢，熟悉起源的可能就注意到这很像是起源引擎的资源文件，但用通用的起源工具是无法打开的，因此这里就用到了上面说到的`Titanfall VPK tool`


1. 打开Titanfall VPK Tool，点击左上角File->Open
    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213113209.png)

2. 找到`\Titanfall2\vpk\englishclient_mp_common.bsp.pak000_dir.vpk`打开即可
    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213113515.png)

    >打开englishXXXX相当于打开了对应的clientXXXX，所以这里我们选择`englishclient_mp_common.bsp.pak000_dir.vpk`也就相当于选择打开了`client_mp_common.bsp.pak000_000.vpk`和`englishclient_mp_common.bsp.pak000_dir.vpk`这一对文件。

3. 打开之后就能看到vpk文件里面的内容了
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213113841.png)

4. 我们不需要想太多，为了后续方便提取文件我们将全部文件导出为好，点击`Extract all`
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213114036.png)

   新建个文件架存储导出的所有文件，图中为例存储到commonFile空文件夹中
    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213114245.png)

    等待导出完成点击ok，这样就得到了vpk文件中的资源文件
    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213114444.png)

5. 取得我们想要制作皮肤的武器模型位置，以car武器为例（其他武器位置请查看NoSkill的文档），模型位置在刚刚导出文件中的`\models\weapons\car101`的文件夹中，另外也请额外留意该武器模型的路径，以后我们还会用到
   
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213114823.png)
    
    其中ptpov_XXX开头的mdl文件是第一人称的武器模型，w_XXX开头的mdl文件是第三人称的武器模型，第一人称的模型肯定是最精细的，我们应该使用ptpov_XXX文件来作为模型设计皮肤。

   当然并不是说w_XXX文件就没用了，后面我们仍然需要用到。**因此这里需要将这两个文件都做好备份。**

6. 用Legion工具来提取mdl文件中的模型至通用模型文件格式。打开我们准备好的Legion工具，打开之后先点击`Settings`
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213115822.png)

   按照下图进行设置，确保和你的设置无误
    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213115917.png)

    设置好后关闭`Settings`窗口

    然后点击`Titanfall 2`
    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213120206.png)

    显示出如图的窗口，我们将上面准备好的ptpov文件直接拖进去
    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213120348.png)

    拖进去不会有任何提示，但实际没有意外的话Legion已经提取出模型文件了

    你可以在Legion程序同目录下的`exported_files`文件夹内找到导出的文件,如图例
    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213120734.png)

    这个.smd文件便是我们需要的武器模型文件。至此我们得到了武器的通用模型格式文件。但为了方便后续制作皮肤我们还得处理一下该模型文件。

### 获取武器模型对应贴图文件
上面步骤中我们得到了武器的模型文件，但为了方便制作皮肤我们往往需要参考武器原本的贴图，那么这就需要获取游戏原本武器贴图资源文件了。

1. 打开legion，点击`Load File`,选择资源文件
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213130744.png)

   我们要打开`\Titanfall2\r2\paks\Win64\common.rpak`该文件，里面包含了不少武器贴图文件。
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213131013.png)

   打开之后legion会如图显示出该文件内的内容
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213131054.png)

   我们在上方搜索框搜索想要的武器贴图名字，例如car的贴图名为car_smg
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213131200.png)

   双击选中项进行导出，当Status变为Exported表示导出成功
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213131300.png)

   我们一样打开legion程序同目录下的`exported_files`文件夹找到我们刚导出的内容，如图
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220213131442.png)
   
   这些便是武器的贴图文件，包含了基础颜色贴图法线贴图AO贴图等。若不懂有什么作用请自行搜索了解，这里不再细讲。

### 处理模型文件
我们需要对已经提取出来的.smd模型文件进行处理，方便我们后续导入到其他软件制作皮肤。
1. 启动Blender 新建一个常规项目
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215103955.png)
2. 按图步骤导入我们的上面提取出的模型文件
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215104108.png)

   如果你是第一次使用Blender你可能会发现你没有这个导入选项，这是因为你没有装起源引擎工具，下面演示如何下载安装该工具组

   1. 打开[BLENDER SOURCE TOOLS](http://steamreview.org/BlenderSourceTools/)该网站，点击`DOWNLOAD`按钮下载工具文件。
   2. 下载后不需要解压这个文件，回到Blender，点击 编辑->偏好设置->插件->安装 找到你下载好的工具文件安装。安装好后找到`Blender Source Tools`勾选启用。
    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215105022.png)
    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215105129.png)
    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215105209.png)
   3. 保存设置重启Blender。这样你就能导入.smd模型文件了,回到上面的第二步。
3. 选中之前导出的模型文件，导入进blender
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215105534.png)

   成功之后就能看到模型了

    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215105647.png)

    右边也会显示出集合，我们可以删除掉不需要的集合比如动画光源相机之类的，只留下我们想要的模型

    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215105904.png)
4. 处理模型，一般来说为了方便绘制皮肤我们把弹夹瞄准镜之类的模型分开来比较好，好在这些模型本来就分开了，我们只需要选中对应的按G拖动就行了

    可以处理成如图

    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215110415.png)
5.  接下来我们要保存为其他通用模型格式方便我们导入另外的模型贴图绘制软件，这里导出为.obj格式

    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215110601.png)

    自己随便起个名字，导出到自己想要的路径即可。
    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215110958.png)

    这也就完成模型文件的处理了。可以进入绘制贴图制作皮肤环节
### 模型皮肤贴图制作
1. 打开Adobe Substance 3D Painter，新建个项目（快捷键Ctrl+N)
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215112510.png)

   文件选择刚刚导出的obj文件，其他和如图设置即可

   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215112626.png)

   点击ok即可
2. 新建完后应该就能看到模型了如图
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215112739.png)

   右边纹理集选择对应的模型，就可以给对应的模型绘制贴图了

   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215112842.png)

   然后还可以导入上面我们提取出来的贴图文件应用

   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215113135.png)

   **受篇幅限制我这里不会也不可能细致讲sp(Substance 3D Painter)的功能和使用方法的，请大家自行网上搜索教程学习，这里只简单一笔带过**

   >sp只能绘制静态的贴图，而我们要实现的动态皮肤实际上是由一帧帧的静态贴图组合而成。因此要做动态皮肤需要提前构思好皮肤如何制作，比如我大部分动态皮肤的思路都是先绘制好基础的静态贴图，然后再在静态贴图上放个视频或动画或gif，合成之后再在pr里分为一帧帧。

    >注意我们做的贴图分辨率为2048x2048即可，游戏原本贴图的分辨率也是这个

   如图，当我们绘制好基础皮肤后我们需要导出贴图

   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215114256.png)

   有两种方式，一种直接sp导出，还有一种经由sp导出到pr，再在pr处理好后导出，我们最终目标都是获取静态贴图。
    - sp导出贴图：

        ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215114542.png)

        然后如图设置，选择你要导出的贴图，因为vtf制作的皮肤只有basecolor贴图生效，所以我们只需要导出basecolor贴图就行了，点击导出

        ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215114718.png)

        导出成功即可得到贴图文件

        ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215114938.png)

    - 实际上为了更好的效果我们还需要经过ps和pr处理，所以大部分情况会选择导出到ps先
        
        如图导出至ps，这要求你已经装好了ps而且不是绿色版那种

        ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215114502.png)

        会提示你执行脚本，允许即可，然后就可以导入进ps了。按照你自己需求想法修改皮肤贴图
        
        ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215120204.png)

        **推荐在使用sp绘制贴图时候就做好遮罩图层，方便后面加上一些视频美观不会那么突兀，sp导出到ps也是同样会分图层的，然后ps在讲贴图文件保存成psd，psd文件再导入到pr里也是可以分图层的，这样在pr里就会十分方便了。**

    其实到这里如果你只是做静态皮肤这里就已经完成了皮肤制作了。可以进入皮肤处理打包环节了。不过我们这里是做动态皮肤所以当然还有很多东西要做咯

### 处理为动态皮肤贴图

前面其实已经简单提到过了动态皮肤的原理，这里细致讲讲吧：

类同于起源引擎动画贴图的制作，动画贴图就是由很多张图片（也就是帧）组成，按顺序播放之后就会形成动画动态的效果，播放是循环的，因此还需要做好首尾连贯拼接处理。在起源引擎中可以将这一系列的帧打包为vtf文件。如果是静态皮肤只有一张贴图便足够，但动画贴图就需要很多张贴图来组成帧，比如若想要播放贴图动画3秒，一秒30帧，那么就一共需要90帧贴图。

我们的思路很简单，先把本是一张图片的贴图做成视频，视频的播放效果便是我们想要的动态效果，做好首尾循环处理，最后将视频导出拆分一帧帧，打包为vtf文件，塞到游戏里。

如果很难理解上面说的话，可以参考我以前做的皮肤的 [R201动态皮肤演示视频](https://www.bilibili.com/video/BV1iy4y1g7kP) 理解。p1是展示，p2是贴图做成视频的样子，都看一下就应该能理解了。尤其是p2一定要看一下!

接下来用我car动态皮肤的制作流程作为示例吧，接下来会讲的稍微简单一些，因为理解了原理就很好做动态皮肤了，可以根据自己的想法来不需要和我一样

使用Adobe Premiere Pro新建个项目，导入我们上面从ps导出保存的psd贴图文件作为素材

然后处理一下加入一些动画素材或者视频素材，比如我的斯卡蒂系列皮肤就会加入live2d的视频素材做成动画
   
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215180905.png)

   像上图那样活用轨道和轨道遮罩键还有pr里面带的转场效果，就能做出很不错的效果

![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/动画1.gif)

![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/动画2.gif)

 好跳过制作的详细步骤，我们继续讲导出了。

导出设置如图，关键的几个设置是：
    
要设置格式为JPEG 然后保证分辨率一致，还有就是**帧数** 帧数太高的话会导致帧画面太多，贴图文件体积大，我们所做的皮肤文件体积是有上限的，基本要保证最后所有帧图片加起来的体积不超过300MB，单个vtf文件体积不能超过1GB，体积大小取决于总帧数，一般来说保证总共帧数不超过300帧为好。我个人偏向于每秒30帧25帧这样。

![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215183831.png)

导出渲染完后你就会得到一堆序列图片帧了，如图
    
![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215184459.png)

注意文件命名要按帧顺序从小到大来，不然之后导入vtf文件顺序错乱的话会导致动画播放顺序错乱。

然后你就会发现每张图片都几乎要3~5MB，那么多张图片加起来总体积肯定是太大了不能打包。那么要怎么办，接下来就是得进行压缩了。

### 压缩皮肤贴图

我们可以使用一些压缩图片的方法牺牲一点质量获取更少的体积。我用了很多压缩图片的方法工具，最后还是发现使用`Caesium` 这个软件好。综合考虑压缩耗时体积质量应该是比较好的这个软件。

![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220215185120.png)

一般来说品质设置成90就可以了，觉得不满意的话可以再自己调调。设定好导出路径之类的就可以压缩了。

压缩完之后我们就得到了体积较小的皮肤文件，然后就可以进入下一步了。

### 打包使用皮肤文件
这一步中的操作会比较复杂，但跟着教程走应该没什么问题

#### 生成vtf文件
首先我们需要将上面做好的皮肤贴图打包成vtf文件

1. 打开VTFEdit，根据系统是多少位的启动对应的版本
   
2. 按顺序点击File->Import
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220219101852.png)

3. 弹出文件选择界面，找到我们压缩好的皮肤贴图文件，选中全部贴图文件，Ctrl+A全选，点击打开
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220219102215.png)

4. 之后会弹出导入设置页面，不懂的话根据我下图的设置来即可
   
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220219102618.png)

   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220219102645.png)

   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220219102707.png)

   点击ok即可开始导入
5. 然后你就会发现程序没有响应，**这是正常的**，VTFEdit正在处理皮肤文件，我们不需要其他操作，等待它导入完成就行。
   
    这个过程的时间是很长的，期间还会占用大量内存空间。不同贴图数量体积分辨率花费时间不同，比如我这270帧图片导入往往要花上20分钟多。
   
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220219103007.png)

6. 导入完成之后应该就可以从右边的界面预览到贴图了。
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220219112154.png)

   点击Play 能预览播放，当然它这里播放的帧数是慢点的，能动就行。

7. 保存vtf文件，点击File->Save as
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220219112505.png)

   自己随便起个名字，保存到自己想要的路径，这样就打包好vtf文件了。

   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220219112653.png)

   保存好这个vtf文件，多备份几个，免得不小心删除了重新导入又要花费很长时间。

   我们后续步骤会再用到这个文件

#### 编写vmt文件
接下来编写vmt文件，新建个记事本txt文件，修改后缀名为.vmt,然后用编辑器打开，往里面写如下内容：

```
"basic"
{
	"$surfaceprop" "metal"
	"$basetexture" "models\XXX" //贴图路径
	
	"Proxies"
	{
		AnimatedTexture
		{
			animatedTextureVar $basetexture
			animatedTextureFrameNumVar $frame
			animatedTextureFrameRate 30  //每秒帧数
		}
	}
}
```
其中这个 贴图路径 `"$basetexture"`是指我们上面解包englishcilent文件里的路径，后面会回来详细介绍。先不用急，继续按顺序阅读。

#### 修改mdl文件
vtf文件弄好后我们需要修改游戏武器模型的mdl文件的十六进制，让它指向我们的皮肤文件

还记得我们上面用到的两个mdl文件吗，这里就又要用上了。先拷贝一份出来，用于接下来的修改。继续用car的来举例演示。
1. 用 Hex Editor Neo 打开 ptpov_XXX.mdl 和 w_XXX.mdl文件
    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220219120036.png)
2. 使用Ctrl + F 搜索"models" 分别在两个mdl文件中，找到形如图中的位置，这里以ptpov_XXX.mdl文件举例
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220219120317.png)

3. 注意图中划线的部分，他们都指的是在我们解包englishclient的文件中的路径，你可以理解为这个路径就是贴图文件的路径
   
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220219120545.png)

    红色划线：`.models\weapons_r2\car_smg\CAR_smg`，指的是原厂贴图的路径

    黑色划线：`.models\weapons_r2\car_smg\CAR_smg_skin_31`，指的是除开原厂贴图和精英皮肤的其他皮肤贴图路口

    如果你按照这个路径去解包出的文件里面找是找不到的，毕竟这是重生魔改过的起源。很多地方还是不一样的。

4. 为了使用我们做的自定义皮肤，我们需要修改这划线的部分，使其指向我们的vmt文件。根据你的需求，如果想要替换原厂皮肤就修改红色划线部分的路径，如果想要修改除开原厂贴图和精英皮肤的其他皮肤就修改黑色划线的部分。当然你也可以两个都改。改路径有个非常重要的要求，**要求保证路径长度和原来一样**

    比如原路径为`.models\weapons_r2\car_smg\CAR_smg`，一共33个字符长度

    那我修改后的路径可以为`.models\weapons_r2\car_smg\car.vmt`，vmt文件命名为CAR.vmt

    或 `.models\weapons_r2\car_smg\abc.vmt`，vmt文件命名为abc.vmt

    或 `.models\weapons_r2\car\Skin\cd.vmt`，vmt文件命名为cd.vmt

    要求就是总长度和原来的一样，指向vmt文件，否则会破环mdl文件游戏无法识别。

    在这里我举例只修改原厂皮肤的情况，那我要修改红色划线部分内容，可以修改为`.models\weapons_r2\car_smg\car.vmt`

    ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220220124146.png)

    红色字体部分就是修改过的部分。

    **注意注意注意！！ptpov_XXX.mdl 和 w_XXX.mdl两个文件都要进行同样的修改** 

    >ptpov_XXX.mdl文件是第一人称的武器模型 ，w_XXX.mdl文件是第三人称的模型

   这样才能让第一人称的武器模型和第三人称的武器模型都正常显示导入的mod皮肤。

   保存好这两个修改好的mdl文件，接下来我们还需要用上。

#### 按照路径配置皮肤文件布局

通过上面的步骤设置了皮肤vmt文件的路径，请记住你设置的文件路径，接下来需要根据设置的路径放置皮肤文件。

<!-- 上面的例子中我们设置的路径为`.models\weapons_r2\car_smg\CAR.vmt`,我们就按这个路径为例子继续讲解。 -->

我们接下来要按照给定的文件布局格式放置皮肤文件，以方便导入打包到原本的游戏文件。

1. 新建一个文件夹方便存放文件。在这个文件夹里面按照以下给定的格式新建文件夹：
```
   |-- 你新建的文件夹名
      |-- materials
      |-- models
```
   肯定有人好奇会问为什么要这样设置文件夹布局，还记得之前解包vpk文件后的文件布局么，我们这里所做的就是配置好一个与原来vpk内文件布局相同的布局，好让之后打包时能够按照文件布局替换对应的文件。

2. 按照你在取出的武器模型mdl文件时得到的[路径](#获得武器模型文件)，放置你修改好后的mdl文件，变成类似下面的文件布局
```
   |-- 你新建的文件夹名
      |-- materials
      |-- models
          |-- weapons
               |-- car101
                  |-- ptpov_car101.mdl
                  |-- w_car101.mdl
```
3. 按照你上面编辑mdl文件时设置的[路径](#修改mdl文件)，放置你编写的vmt文件，变成类似下面的文件布局
```  
   |-- 你新建的文件夹名
      |-- materials
      |   |-- models
      |       |-- weapons_r2
      |           |-- car_smg
      |               |-- car.vmt
      |-- models
          |-- weapons
               |-- car101
                  |-- ptpov_car101.mdl
                  |-- w_car101.mdl
```

4. 把[上面](#生成vtf文件)生成的vtf文件也放进来，放在.vmt文件同目录下为好，如下面所示
``` 
   |-- 你新建的文件夹名
      |-- materials
      |   |-- models
      |       |-- weapons_r2
      |           |-- car_smg
      |               |-- car.vmt
      |               |-- car_base.vtf
      |-- models
          |-- weapons
               |-- car101
                  |-- ptpov_car101.mdl
                  |-- w_car101.mdl
```

5. 我们现在已经把模型文件和皮肤文件都放好了，需要再编写vmt文件重新设置一下贴图路径，打开vmt文件修改：

   注意到这一行参数

   ```
      "$basetexture" "models\XXX" //贴图路径
   ```

   我们要使其指向我们的vtf皮肤文件，那么这个路径就是需要修改。更改为：
   ```
      "$basetexture" "models\weapons_r2\car_smg\car_base" //贴图路径
   ```
   路径是根据我们上面的文件布局得到的，注意路径前面不需要加上`materials\`，且指向的vtf文件不需要加上扩展名

   修改好后保存。

这样一来皮肤文件就弄好了。

**接下来我们有两种方式打包使用皮肤，各有优缺点**
- 方式1 适用于原版游戏，多人单人都能正常用，装了北极星客户端也能用，缺点就是每次装多个皮肤的话都得每个皮肤一起再打包，使用者需要自己打包，很麻烦，而且皮肤效果会有出入，偏白。
- 方式2 只适用于安装了北极星客户端下，只有北极星游玩下才会生效，优点是皮肤文件是单独打包的，非常方便管理，使用者只需要复制粘贴就可以了，不用直接删除就行。
  
#### （方式1）使用RSPNVPK打包皮肤文件并安装使用

这种情况下使用者需要完整执行下面的步骤

1. 解压我们下载好的RSPNVPK

2. 从游戏目录的vpk文件夹里复制一份`englishclient_mp_common.bsp.pak000_dir.vpk`文件到解压好的RSPNVPK根目录下，并创建一个同名的文件夹(不包括".vpk") 

   如图：

   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316163855.png)

3. 打开englishclient_mp_common.bsp.pak000_dir文件夹，把我们的上面弄好的皮肤mod文件放进去，

   注意不是直接你上面皮肤文件夹直接丢进去，而是把你文件夹里的model文件夹和materials文件夹放进去，文件布局如下：
```
|-- englishclient_mp_common.bsp.pak000_dir
            |-- materials
            |   |-- models
            |       |-- weapons_r2
            |           |-- car_smg
            |               |-- car.vmt
            |               |-- car_base.vtf
            |-- models
               |-- weapons
                     |-- car101
                        |-- ptpov_car101.mdl
                        |-- w_car101.mdl
```
4. 回到RSPNVPK, 拖动`englishclient_mp_common.bsp.pak000_dir.vpk`文件到`RSPNVPK.exe` 释放打开
   
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/1621skin.gif)


5. 如图所示，程序会自动读取到皮肤文件，
   
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316165921.png)

   此时输入y并回车可以进行备份，并进行打包

6. 等待程序显示如图提示完成后，按回车结束即可。
   
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316170026.png)

7. 此时RSPNVPK下便会重新生成两个vpk文件

   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316170158.png)

   这两个文件就是我们打包好的，包含皮肤mod的vpk文件

接下来就很简单了，把上面生成的两个文件覆盖到游戏原来的vpk文件夹即可，路径`Titanfall2\vpk`

(注意备份！！！)

![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316170727.png)

大功告成，然后启动游戏就可以看到皮肤效果啦！

![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316170903.png)

#### （方式2，作为北极星模组）使用TitanfallVPK打包皮肤成为北极星mod

我们需要再次用到Titanfall VPK Tool 这个工具，用其自带的功能直接打包皮肤文件为独立的vpk

1. 打开Titanfall VPK Tool，按如图点击`repacker`
   
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316172436.png)

2. 弹出如图的对话框，第一个红框设置要打包文件夹路径，第二个红框设置打包导出vpk文件的路径

   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316173712.png)

   然后点击build vpk即可开始打包

   第一个红框选的文件夹就是我们[上面配置好的皮肤文件](#按照路径配置皮肤文件布局), 为了方便理解我这边再给大家列出我图中选中的皮肤文件夹布局
```
   |-- skadiCARNFV
      |-- materials
      |   |-- models
      |       |-- weapons_r2
      |           |-- car_smg
      |               |-- car_base.vtf
      |               |-- car.vmt
      |-- models
         |-- weapons
               |-- car101
                  |-- ptpov_car101.mdl
                  |-- w_car101.mdl
```

3. 如图提示打包完成后，我们便可以在设置的导出路径中得到打包好的两个vpk文件
   
   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316174323.png)

   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316174439.png)

4. 接下来我们需要给这两个文件重新命名
   
   注意不要弄错了

   - 不以“_dir.vpk”结尾的文件命名为`client_mp_common.bsp.pak000_000.vpk`
   - 以“_dir.vpk”结尾的文件命名为`englishclient_mp_common.bsp.pak000_dir.vpk`
  
   即变成

   ![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316174850.png)

   这样作为皮肤文件就打包好了，但是我们要把它变成北极星能识别的mod的话需要接下来的几个操作。

5. 我们需要按照北极星的要求格式制作个北极星mod
   
   1. 新建个文件夹，文件名格式推荐为 `作者.mod名字`
   
      比如我的car皮肤mod，可以把文件夹名字命名为 `HK560.CarSkadiAnimatedSkinFV`
   2. 然后在这个文件夹里创建一个`mod.json` 文件，并打开编辑
   
      写入以下内容：
```
{
	"Name" : "CAR Skadi Animated Skin Full Version 0.1",
	"Description" : "Made by HK560.",
	"Version": "0.0.1",
	"LoadPriority": 4
}
```
   其中`"Name"`后面的参数是你的mod的名字，可以自己改。`"Description"`是描述，`"Version"`是mod的版本号，`"LoadPriority"`是mod加载优先级

   除了`"LoadPriority"`最好不要改以外，其他你可以按照自己想法改，注意不支持中文！

   写好后保存。

>附：北极星mod文档可以查看[这里](https://r2northstar.readthedocs.io/en/latest/guides/publishing.html)

   3. 然后再在这个文件夹下新建一个文件夹，文件夹名为`vpk`, 把我们上面打包好的那两个vpk文件丢进去，形成如下的文件布局
```
   |-- HK560.CarSkadiAnimatedSkinFV
       |-- mod.json
       |-- vpk
           |-- client_mp_common.bsp.pak000_000.vpk
           |-- englishclient_mp_common.bsp.pak000_dir.vpk
```
   这样就可以了，这整个文件夹就是一个符合北极星要求的mod。分享给别人的话也只需要打包这整个文件夹就行了。


#### （方式2，作为北极星模组）安装使用打包为北极星mod的皮肤文件

很简单，确保你的游戏已经安装好了北极星客户端，打开游戏根目录该路径`\Titanfall2\R2Northstar\mods`

在这个mods文件夹下存放着北极星官方的模组文件，也可以存放其他符合北极星mod格式的模组文件

把我们上面弄好的皮肤mod文件夹放进去即可

![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316181101.png)

（我这里mods文件夹还装了很多其他模组，不用在意）

然后正常启动北极星即可！正常的话你可以在北极星`模组mods`菜单里看到你装的mod。

![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316181342.png)

![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/20220316181454.png)

![](https://cdn.jsdelivr.net/gh/HK560/MyPicHub@master/res/pic/3213skin.gif)

到此教程结束！

## 后言补充

这篇教程断断续续写了好久，也不知道写的能不能让大家看懂，有不懂的地方可以留言评论，我尽量解答。

真的非常感激国内外那些为泰坦陨落2社区和mod社区做出贡献的大牛们，你们的付出为这个游戏这个社区再次增加了活力，由衷感谢你们！



**附：**
- [北极星项目NorthStar](https://github.com/R2Northstar)
- [北极星CN项目NorthStarCN](https://github.com/R2NorthstarCN)