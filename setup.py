import cx_Freeze

executables = [cx_Freeze.Executable("flappybird.py",base="Win32GUI")]

cx_Freeze.setup(
    name="Flappy Bird",
    version="1.0.1",
    options={"build_exe": {"packages":["pygame","os","random"],#'include_msvcr' : True,
                           "include_files":["F:\\GameDev\\Assets\\2D\\FlappyBird\\Flappy bird\\PNG\\bg.png","F:\\GameDev\\Assets\\2D\\FlappyBird\\Flappy bird\\PNG\\logo.png","F:\\GameDev\\Assets\\2D\\FlappyBird\\Flappy bird\\PNG\\pipe.png","F:\\GameDev\\Assets\\2D\\FlappyBird\\Flappy bird\\PNG\\play.png","F:\\GameDev\\Assets\\2D\\FlappyBird\\Flappy bird\\PNG\\flappybird\\Flappy-Bird.ttf","F:\\GameDev\\Assets\\2D\\FlappyBird\\Flappy bird\\PNG\\frame-1.png","F:\\GameDev\\Assets\\2D\\FlappyBird\\Flappy bird\\PNG\\frame-2.png","F:\\GameDev\\Assets\\2D\\FlappyBird\\Flappy bird\\PNG\\frame-3.png","F:\\GameDev\\Assets\\2D\\FlappyBird\\Flappy bird\\PNG\\frame-4.png"]}},
    executables = executables,


    )