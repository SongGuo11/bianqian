# 如何将项目上传到GitHub

## 步骤1：在GitHub上创建仓库

1. 访问 [GitHub](https://github.com/) 并使用你的账户登录
2. 点击右上角的 "+" 号，选择 "New repository"
3. 为仓库起一个名字（例如：bianqian）
4. 选择设为公开（Public）或私有（Private）
5. **重要**：不要初始化 README 文件，也不要添加 .gitignore 或许可证
6. 点击 "Create repository"

## 步骤2：获取仓库地址

创建仓库后，你会看到类似下面的页面，复制 HTTPS 地址：
```
https://github.com/SongGuo11/你的仓库名.git
```

## 步骤3：添加远程仓库并推送

在终端中执行以下命令（请将 `你的仓库名` 替换为实际的仓库名）：

```bash
git remote add origin https://github.com/SongGuo11/你的仓库名.git
git branch -M main
git push -u origin main
```

## 完成

现在你的代码已经成功上传到GitHub仓库了！