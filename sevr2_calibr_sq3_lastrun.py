#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on Tue Dec 30 18:57:55 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = '4_calibr_sum'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'name ': '',
    'gender ': '',
    'ag': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1710, 1107]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['name'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/arinasevruk/Desktop/Exp/MyExp/sevr2_calibr_sq3_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=True,
            monitor='testMonitor', color=[-0.2314, -0.2314, -0.2314], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-0.2314, -0.2314, -0.2314]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Подождите немного, сейчас запустится')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('main_instr_key') is None:
        # initialise main_instr_key
        main_instr_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='main_instr_key',
        )
    if deviceManager.getDevice('BJW_key_resp') is None:
        # initialise BJW_key_resp
        BJW_key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='BJW_key_resp',
        )
    if deviceManager.getDevice('resp_instr') is None:
        # initialise resp_instr
        resp_instr = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resp_instr',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('resp_tren') is None:
        # initialise resp_tren
        resp_tren = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resp_tren',
        )
    if deviceManager.getDevice('reesp_instr') is None:
        # initialise reesp_instr
        reesp_instr = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='reesp_instr',
        )
    if deviceManager.getDevice('resp') is None:
        # initialise resp
        resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resp',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('gp_key_resp') is None:
        # initialise gp_key_resp
        gp_key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='gp_key_resp',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Main_instr" ---
    main_instr_text = visual.TextStim(win=win, name='main_instr_text',
        text='Добрый день! Приглашаем принять участие в эксперименте и спасти одну магистерскую жизнь!\n\nСтуденты РАНХиГС, которые хотят получить баллы за участие, смогут оставить сведения о себе в конце эксперимента. \n\nДля того, чтобы начать, нажмите на пробел',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    main_instr_key = keyboard.Keyboard(deviceName='main_instr_key')
    
    # --- Initialize components for Routine "instr_BJW" ---
    BJW_inst_text = visual.TextStim(win=win, name='BJW_inst_text',
        text='Вам будут предложены утверждения (13). \n\nПожалуйста, оцените, насколько каждое утверждение соответствует вашему мнению. \n\nДля этого перетащите красный кружок мышкой на ту позицию шкалы, которая лучше всего отражает ваше отношение.\n\nМы исследуем мир и себя в нем. Пожалуйста, отвечайте честно и вдумчиво.\n\nНажмите "пробел", чтобы приступить.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    BJW_key_resp = keyboard.Keyboard(deviceName='BJW_key_resp')
    
    # --- Initialize components for Routine "BJW" ---
    BJW_slider = visual.Slider(win=win, name='BJW_slider',
        startValue=3, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
        labels=['Совершенно не согласен','Скорее не согласен','Не уверен', 'Скорее согласен', 'Совершенно согласен'], ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.02,
        flip=True, ori=0.0, depth=0, readOnly=False)
    BJW_text = visual.TextStim(win=win, name='BJW_text',
        text='',
        font='Arial',
        pos=(0, 0.2), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "instr" ---
    text_instr = visual.TextStim(win=win, name='text_instr',
        text='Вам нужно будет сравнивать квадраты по размеру. \nЕсли больше правый квадрат, нажмите кнопку "вправо", еcли левый - то "влево".\n\nНажмите "пробел", чтобы приступить.\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    resp_instr = keyboard.Keyboard(deviceName='resp_instr')
    
    # --- Initialize components for Routine "instr_2" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Сейчас тренировочный этап. \nВам нужно будет сравнивать квадраты по величине.\n\nЕсли больше правый квадрат, нажмите "вправо", если левый - то "влево".\nЕсли готовы - нажмите пробел и переходите к сравнению.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "tren" ---
    pol_1 = visual.Rect(
        win=win, name='pol_1',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=1.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-1.0, interpolate=True)
    pol_2 = visual.Rect(
        win=win, name='pol_2',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=1.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-2.0, interpolate=True)
    resp_tren = keyboard.Keyboard(deviceName='resp_tren')
    text_tren = visual.TextStim(win=win, name='text_tren',
        text='Если больше правый квадрат, нажмите "вправо", если левый - то "влево"',
        font='Arial',
        pos=(0, 0.35), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "fb_tren" ---
    # Run 'Begin Experiment' code from code_tr_2
    msg = ''
    text_fb_tren = visual.TextStim(win=win, name='text_fb_tren',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "instr3" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text='А теперь - основной этап.  Но время  на выполнение  каждого задания будет ограничено. \nЕсли готовы - нажмите на пробел.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    reesp_instr = keyboard.Keyboard(deviceName='reesp_instr')
    
    # --- Initialize components for Routine "task_L" ---
    sq_1 = visual.Rect(
        win=win, name='sq_1',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=1.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=[1.0000, 1.0000, 1.0000],
        opacity=1.0, depth=0.0, interpolate=True)
    sq_2 = visual.Rect(
        win=win, name='sq_2',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=1.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-1.0, interpolate=True)
    resp = keyboard.Keyboard(deviceName='resp')
    text = visual.TextStim(win=win, name='text',
        text='Если больше правый квадрат, нажмите "вправо", если левый - то "влево"',
        font='Arial',
        pos=(0, 0.35), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "fb_task" ---
    # Run 'Begin Experiment' code from code_4
    msg = ''
    corr_sum = 0
    all_rt = []
    SD_rt = []
    np = None
    text_fb_task = visual.TextStim(win=win, name='text_fb_task',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "slider" ---
    sl_h = visual.Slider(win=win, name='sl_h',
        startValue=5, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
        labels=['совсем нет','очень'], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9), granularity=0.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=True, ori=0.0, depth=0, readOnly=False)
    text_sl = visual.TextStim(win=win, name='text_sl',
        text='',
        font='Arial',
        pos=(0, 0.2), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "fin_sum" ---
    # Run 'Begin Experiment' code from code
    final_sum = ''
    mean_rt = 0
    SD_rt = 0
    text_5 = visual.TextStim(win=win, name='text_5',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "Get_points" ---
    textbox = visual.TextBox2(
         win, text='Введите номер строки для учета баллов. Затем нажмите на пробел для завершения:', placeholder='Поле ввода:', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox',
         depth=0, autoLog=True,
    )
    gp_key_resp = keyboard.Keyboard(deviceName='gp_key_resp')
    
    # --- Initialize components for Routine "thanks" ---
    text_th = visual.TextStim(win=win, name='text_th',
        text='Спасибо за участие!\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Main_instr" ---
    # create an object to store info about Routine Main_instr
    Main_instr = data.Routine(
        name='Main_instr',
        components=[main_instr_text, main_instr_key],
    )
    Main_instr.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for main_instr_key
    main_instr_key.keys = []
    main_instr_key.rt = []
    _main_instr_key_allKeys = []
    # store start times for Main_instr
    Main_instr.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Main_instr.tStart = globalClock.getTime(format='float')
    Main_instr.status = STARTED
    thisExp.addData('Main_instr.started', Main_instr.tStart)
    Main_instr.maxDuration = None
    # keep track of which components have finished
    Main_instrComponents = Main_instr.components
    for thisComponent in Main_instr.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Main_instr" ---
    Main_instr.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *main_instr_text* updates
        
        # if main_instr_text is starting this frame...
        if main_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_instr_text.frameNStart = frameN  # exact frame index
            main_instr_text.tStart = t  # local t and not account for scr refresh
            main_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_instr_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'main_instr_text.started')
            # update status
            main_instr_text.status = STARTED
            main_instr_text.setAutoDraw(True)
        
        # if main_instr_text is active this frame...
        if main_instr_text.status == STARTED:
            # update params
            pass
        
        # *main_instr_key* updates
        waitOnFlip = False
        
        # if main_instr_key is starting this frame...
        if main_instr_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_instr_key.frameNStart = frameN  # exact frame index
            main_instr_key.tStart = t  # local t and not account for scr refresh
            main_instr_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_instr_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'main_instr_key.started')
            # update status
            main_instr_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(main_instr_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(main_instr_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if main_instr_key.status == STARTED and not waitOnFlip:
            theseKeys = main_instr_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _main_instr_key_allKeys.extend(theseKeys)
            if len(_main_instr_key_allKeys):
                main_instr_key.keys = _main_instr_key_allKeys[-1].name  # just the last key pressed
                main_instr_key.rt = _main_instr_key_allKeys[-1].rt
                main_instr_key.duration = _main_instr_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Main_instr,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Main_instr.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Main_instr.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Main_instr" ---
    for thisComponent in Main_instr.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Main_instr
    Main_instr.tStop = globalClock.getTime(format='float')
    Main_instr.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Main_instr.stopped', Main_instr.tStop)
    # check responses
    if main_instr_key.keys in ['', [], None]:  # No response was made
        main_instr_key.keys = None
    thisExp.addData('main_instr_key.keys',main_instr_key.keys)
    if main_instr_key.keys != None:  # we had a response
        thisExp.addData('main_instr_key.rt', main_instr_key.rt)
        thisExp.addData('main_instr_key.duration', main_instr_key.duration)
    thisExp.nextEntry()
    # the Routine "Main_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instr_BJW" ---
    # create an object to store info about Routine instr_BJW
    instr_BJW = data.Routine(
        name='instr_BJW',
        components=[BJW_inst_text, BJW_key_resp],
    )
    instr_BJW.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for BJW_key_resp
    BJW_key_resp.keys = []
    BJW_key_resp.rt = []
    _BJW_key_resp_allKeys = []
    # store start times for instr_BJW
    instr_BJW.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instr_BJW.tStart = globalClock.getTime(format='float')
    instr_BJW.status = STARTED
    thisExp.addData('instr_BJW.started', instr_BJW.tStart)
    instr_BJW.maxDuration = None
    # keep track of which components have finished
    instr_BJWComponents = instr_BJW.components
    for thisComponent in instr_BJW.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr_BJW" ---
    instr_BJW.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BJW_inst_text* updates
        
        # if BJW_inst_text is starting this frame...
        if BJW_inst_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BJW_inst_text.frameNStart = frameN  # exact frame index
            BJW_inst_text.tStart = t  # local t and not account for scr refresh
            BJW_inst_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BJW_inst_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'BJW_inst_text.started')
            # update status
            BJW_inst_text.status = STARTED
            BJW_inst_text.setAutoDraw(True)
        
        # if BJW_inst_text is active this frame...
        if BJW_inst_text.status == STARTED:
            # update params
            pass
        
        # *BJW_key_resp* updates
        waitOnFlip = False
        
        # if BJW_key_resp is starting this frame...
        if BJW_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BJW_key_resp.frameNStart = frameN  # exact frame index
            BJW_key_resp.tStart = t  # local t and not account for scr refresh
            BJW_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BJW_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'BJW_key_resp.started')
            # update status
            BJW_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(BJW_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(BJW_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if BJW_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = BJW_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _BJW_key_resp_allKeys.extend(theseKeys)
            if len(_BJW_key_resp_allKeys):
                BJW_key_resp.keys = _BJW_key_resp_allKeys[-1].name  # just the last key pressed
                BJW_key_resp.rt = _BJW_key_resp_allKeys[-1].rt
                BJW_key_resp.duration = _BJW_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instr_BJW,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instr_BJW.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_BJW.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr_BJW" ---
    for thisComponent in instr_BJW.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instr_BJW
    instr_BJW.tStop = globalClock.getTime(format='float')
    instr_BJW.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instr_BJW.stopped', instr_BJW.tStop)
    # check responses
    if BJW_key_resp.keys in ['', [], None]:  # No response was made
        BJW_key_resp.keys = None
    thisExp.addData('BJW_key_resp.keys',BJW_key_resp.keys)
    if BJW_key_resp.keys != None:  # we had a response
        thisExp.addData('BJW_key_resp.rt', BJW_key_resp.rt)
        thisExp.addData('BJW_key_resp.duration', BJW_key_resp.duration)
    thisExp.nextEntry()
    # the Routine "instr_BJW" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    BJW_trials = data.TrialHandler2(
        name='BJW_trials',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('BJW.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(BJW_trials)  # add the loop to the experiment
    thisBJW_trial = BJW_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBJW_trial.rgb)
    if thisBJW_trial != None:
        for paramName in thisBJW_trial:
            globals()[paramName] = thisBJW_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisBJW_trial in BJW_trials:
        BJW_trials.status = STARTED
        if hasattr(thisBJW_trial, 'status'):
            thisBJW_trial.status = STARTED
        currentLoop = BJW_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisBJW_trial.rgb)
        if thisBJW_trial != None:
            for paramName in thisBJW_trial:
                globals()[paramName] = thisBJW_trial[paramName]
        
        # --- Prepare to start Routine "BJW" ---
        # create an object to store info about Routine BJW
        BJW = data.Routine(
            name='BJW',
            components=[BJW_slider, BJW_text],
        )
        BJW.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        BJW_slider.reset()
        BJW_text.setText(Text)
        # store start times for BJW
        BJW.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        BJW.tStart = globalClock.getTime(format='float')
        BJW.status = STARTED
        thisExp.addData('BJW.started', BJW.tStart)
        BJW.maxDuration = None
        # keep track of which components have finished
        BJWComponents = BJW.components
        for thisComponent in BJW.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "BJW" ---
        BJW.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBJW_trial, 'status') and thisBJW_trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BJW_slider* updates
            
            # if BJW_slider is starting this frame...
            if BJW_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BJW_slider.frameNStart = frameN  # exact frame index
                BJW_slider.tStart = t  # local t and not account for scr refresh
                BJW_slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BJW_slider, 'tStartRefresh')  # time at next scr refresh
                # update status
                BJW_slider.status = STARTED
                BJW_slider.setAutoDraw(True)
            
            # if BJW_slider is active this frame...
            if BJW_slider.status == STARTED:
                # update params
                pass
            
            # Check BJW_slider for response to end Routine
            if BJW_slider.getRating() is not None and BJW_slider.status == STARTED:
                continueRoutine = False
            
            # *BJW_text* updates
            
            # if BJW_text is starting this frame...
            if BJW_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BJW_text.frameNStart = frameN  # exact frame index
                BJW_text.tStart = t  # local t and not account for scr refresh
                BJW_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BJW_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BJW_text.started')
                # update status
                BJW_text.status = STARTED
                BJW_text.setAutoDraw(True)
            
            # if BJW_text is active this frame...
            if BJW_text.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=BJW,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                BJW.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BJW.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "BJW" ---
        for thisComponent in BJW.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for BJW
        BJW.tStop = globalClock.getTime(format='float')
        BJW.tStopRefresh = tThisFlipGlobal
        thisExp.addData('BJW.stopped', BJW.tStop)
        BJW_trials.addData('BJW_slider.response', BJW_slider.getRating())
        BJW_trials.addData('BJW_slider.rt', BJW_slider.getRT())
        BJW_trials.addData('BJW_slider.history', BJW_slider.getHistory())
        # the Routine "BJW" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisBJW_trial as finished
        if hasattr(thisBJW_trial, 'status'):
            thisBJW_trial.status = FINISHED
        # if awaiting a pause, pause now
        if BJW_trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            BJW_trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'BJW_trials'
    BJW_trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instr" ---
    # create an object to store info about Routine instr
    instr = data.Routine(
        name='instr',
        components=[text_instr, resp_instr],
    )
    instr.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for resp_instr
    resp_instr.keys = []
    resp_instr.rt = []
    _resp_instr_allKeys = []
    # store start times for instr
    instr.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instr.tStart = globalClock.getTime(format='float')
    instr.status = STARTED
    thisExp.addData('instr.started', instr.tStart)
    instr.maxDuration = None
    # keep track of which components have finished
    instrComponents = instr.components
    for thisComponent in instr.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr" ---
    instr.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_instr* updates
        
        # if text_instr is starting this frame...
        if text_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_instr.frameNStart = frameN  # exact frame index
            text_instr.tStart = t  # local t and not account for scr refresh
            text_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_instr, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_instr.status = STARTED
            text_instr.setAutoDraw(True)
        
        # if text_instr is active this frame...
        if text_instr.status == STARTED:
            # update params
            pass
        
        # *resp_instr* updates
        
        # if resp_instr is starting this frame...
        if resp_instr.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_instr.frameNStart = frameN  # exact frame index
            resp_instr.tStart = t  # local t and not account for scr refresh
            resp_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_instr, 'tStartRefresh')  # time at next scr refresh
            # update status
            resp_instr.status = STARTED
            # keyboard checking is just starting
            resp_instr.clock.reset()  # now t=0
        if resp_instr.status == STARTED:
            theseKeys = resp_instr.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
            _resp_instr_allKeys.extend(theseKeys)
            if len(_resp_instr_allKeys):
                resp_instr.keys = _resp_instr_allKeys[-1].name  # just the last key pressed
                resp_instr.rt = _resp_instr_allKeys[-1].rt
                resp_instr.duration = _resp_instr_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instr,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instr.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr" ---
    for thisComponent in instr.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instr
    instr.tStop = globalClock.getTime(format='float')
    instr.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instr.stopped', instr.tStop)
    # check responses
    if resp_instr.keys in ['', [], None]:  # No response was made
        resp_instr.keys = None
    thisExp.addData('resp_instr.keys',resp_instr.keys)
    if resp_instr.keys != None:  # we had a response
        thisExp.addData('resp_instr.rt', resp_instr.rt)
        thisExp.addData('resp_instr.duration', resp_instr.duration)
    thisExp.nextEntry()
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instr_2" ---
    # create an object to store info about Routine instr_2
    instr_2 = data.Routine(
        name='instr_2',
        components=[text_3, key_resp],
    )
    instr_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for instr_2
    instr_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instr_2.tStart = globalClock.getTime(format='float')
    instr_2.status = STARTED
    thisExp.addData('instr_2.started', instr_2.tStart)
    instr_2.maxDuration = None
    # keep track of which components have finished
    instr_2Components = instr_2.components
    for thisComponent in instr_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr_2" ---
    instr_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instr_2,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instr_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr_2" ---
    for thisComponent in instr_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instr_2
    instr_2.tStop = globalClock.getTime(format='float')
    instr_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instr_2.stopped', instr_2.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "instr_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('trening2.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        trials.status = STARTED
        if hasattr(thisTrial, 'status'):
            thisTrial.status = STARTED
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "tren" ---
        # create an object to store info about Routine tren
        tren = data.Routine(
            name='tren',
            components=[pol_1, pol_2, resp_tren, text_tren],
        )
        tren.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        pol_1.setOpacity(op1)
        pol_1.setPos((xPos1, 0))
        pol_1.setSize((w1, w1))
        pol_1.setOri(or1)
        pol_2.setOpacity(op1)
        pol_2.setPos((xPos2, 0))
        pol_2.setSize((w2, w2))
        pol_2.setOri(or2)
        # create starting attributes for resp_tren
        resp_tren.keys = []
        resp_tren.rt = []
        _resp_tren_allKeys = []
        # store start times for tren
        tren.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        tren.tStart = globalClock.getTime(format='float')
        tren.status = STARTED
        thisExp.addData('tren.started', tren.tStart)
        tren.maxDuration = None
        # keep track of which components have finished
        trenComponents = tren.components
        for thisComponent in tren.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "tren" ---
        tren.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pol_1* updates
            
            # if pol_1 is starting this frame...
            if pol_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pol_1.frameNStart = frameN  # exact frame index
                pol_1.tStart = t  # local t and not account for scr refresh
                pol_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pol_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pol_1.started')
                # update status
                pol_1.status = STARTED
                pol_1.setAutoDraw(True)
            
            # if pol_1 is active this frame...
            if pol_1.status == STARTED:
                # update params
                pass
            
            # *pol_2* updates
            
            # if pol_2 is starting this frame...
            if pol_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pol_2.frameNStart = frameN  # exact frame index
                pol_2.tStart = t  # local t and not account for scr refresh
                pol_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pol_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pol_2.started')
                # update status
                pol_2.status = STARTED
                pol_2.setAutoDraw(True)
            
            # if pol_2 is active this frame...
            if pol_2.status == STARTED:
                # update params
                pass
            
            # *resp_tren* updates
            
            # if resp_tren is starting this frame...
            if resp_tren.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_tren.frameNStart = frameN  # exact frame index
                resp_tren.tStart = t  # local t and not account for scr refresh
                resp_tren.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_tren, 'tStartRefresh')  # time at next scr refresh
                # update status
                resp_tren.status = STARTED
                # keyboard checking is just starting
                resp_tren.clock.reset()  # now t=0
            if resp_tren.status == STARTED:
                theseKeys = resp_tren.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
                _resp_tren_allKeys.extend(theseKeys)
                if len(_resp_tren_allKeys):
                    resp_tren.keys = _resp_tren_allKeys[-1].name  # just the last key pressed
                    resp_tren.rt = _resp_tren_allKeys[-1].rt
                    resp_tren.duration = _resp_tren_allKeys[-1].duration
                    # was this correct?
                    if (resp_tren.keys == str(corr_answ)) or (resp_tren.keys == corr_answ):
                        resp_tren.corr = 1
                    else:
                        resp_tren.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_tren* updates
            
            # if text_tren is starting this frame...
            if text_tren.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_tren.frameNStart = frameN  # exact frame index
                text_tren.tStart = t  # local t and not account for scr refresh
                text_tren.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_tren, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_tren.started')
                # update status
                text_tren.status = STARTED
                text_tren.setAutoDraw(True)
            
            # if text_tren is active this frame...
            if text_tren.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=tren,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                tren.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in tren.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "tren" ---
        for thisComponent in tren.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for tren
        tren.tStop = globalClock.getTime(format='float')
        tren.tStopRefresh = tThisFlipGlobal
        thisExp.addData('tren.stopped', tren.tStop)
        # check responses
        if resp_tren.keys in ['', [], None]:  # No response was made
            resp_tren.keys = None
            # was no response the correct answer?!
            if str(corr_answ).lower() == 'none':
               resp_tren.corr = 1;  # correct non-response
            else:
               resp_tren.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('resp_tren.keys',resp_tren.keys)
        trials.addData('resp_tren.corr', resp_tren.corr)
        if resp_tren.keys != None:  # we had a response
            trials.addData('resp_tren.rt', resp_tren.rt)
            trials.addData('resp_tren.duration', resp_tren.duration)
        # the Routine "tren" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fb_tren" ---
        # create an object to store info about Routine fb_tren
        fb_tren = data.Routine(
            name='fb_tren',
            components=[text_fb_tren],
        )
        fb_tren.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_tr_2
        if resp_tren.corr == 1:
            msg = 'Верно!'
            
        else:
            msg = 'Увы('
        text_fb_tren.setText(msg)
        # store start times for fb_tren
        fb_tren.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fb_tren.tStart = globalClock.getTime(format='float')
        fb_tren.status = STARTED
        thisExp.addData('fb_tren.started', fb_tren.tStart)
        fb_tren.maxDuration = None
        # keep track of which components have finished
        fb_trenComponents = fb_tren.components
        for thisComponent in fb_tren.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fb_tren" ---
        fb_tren.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_fb_tren* updates
            
            # if text_fb_tren is starting this frame...
            if text_fb_tren.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_fb_tren.frameNStart = frameN  # exact frame index
                text_fb_tren.tStart = t  # local t and not account for scr refresh
                text_fb_tren.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fb_tren, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_fb_tren.started')
                # update status
                text_fb_tren.status = STARTED
                text_fb_tren.setAutoDraw(True)
            
            # if text_fb_tren is active this frame...
            if text_fb_tren.status == STARTED:
                # update params
                pass
            
            # if text_fb_tren is stopping this frame...
            if text_fb_tren.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_fb_tren.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_fb_tren.tStop = t  # not accounting for scr refresh
                    text_fb_tren.tStopRefresh = tThisFlipGlobal  # on global time
                    text_fb_tren.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_fb_tren.stopped')
                    # update status
                    text_fb_tren.status = FINISHED
                    text_fb_tren.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=fb_tren,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fb_tren.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fb_tren.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fb_tren" ---
        for thisComponent in fb_tren.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fb_tren
        fb_tren.tStop = globalClock.getTime(format='float')
        fb_tren.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fb_tren.stopped', fb_tren.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fb_tren.maxDurationReached:
            routineTimer.addTime(-fb_tren.maxDuration)
        elif fb_tren.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        # mark thisTrial as finished
        if hasattr(thisTrial, 'status'):
            thisTrial.status = FINISHED
        # if awaiting a pause, pause now
        if trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instr3" ---
    # create an object to store info about Routine instr3
    instr3 = data.Routine(
        name='instr3',
        components=[text_4, reesp_instr],
    )
    instr3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for reesp_instr
    reesp_instr.keys = []
    reesp_instr.rt = []
    _reesp_instr_allKeys = []
    # store start times for instr3
    instr3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instr3.tStart = globalClock.getTime(format='float')
    instr3.status = STARTED
    thisExp.addData('instr3.started', instr3.tStart)
    instr3.maxDuration = None
    # keep track of which components have finished
    instr3Components = instr3.components
    for thisComponent in instr3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr3" ---
    instr3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # *reesp_instr* updates
        
        # if reesp_instr is starting this frame...
        if reesp_instr.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reesp_instr.frameNStart = frameN  # exact frame index
            reesp_instr.tStart = t  # local t and not account for scr refresh
            reesp_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reesp_instr, 'tStartRefresh')  # time at next scr refresh
            # update status
            reesp_instr.status = STARTED
            # keyboard checking is just starting
            reesp_instr.clock.reset()  # now t=0
        if reesp_instr.status == STARTED:
            theseKeys = reesp_instr.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _reesp_instr_allKeys.extend(theseKeys)
            if len(_reesp_instr_allKeys):
                reesp_instr.keys = _reesp_instr_allKeys[-1].name  # just the last key pressed
                reesp_instr.rt = _reesp_instr_allKeys[-1].rt
                reesp_instr.duration = _reesp_instr_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instr3,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instr3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr3" ---
    for thisComponent in instr3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instr3
    instr3.tStop = globalClock.getTime(format='float')
    instr3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instr3.stopped', instr3.tStop)
    # check responses
    if reesp_instr.keys in ['', [], None]:  # No response was made
        reesp_instr.keys = None
    thisExp.addData('reesp_instr.keys',reesp_instr.keys)
    if reesp_instr.keys != None:  # we had a response
        thisExp.addData('reesp_instr.rt', reesp_instr.rt)
        thisExp.addData('reesp_instr.duration', reesp_instr.duration)
    thisExp.nextEntry()
    # the Routine "instr3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop_L = data.TrialHandler2(
        name='loop_L',
        nReps=1.0, 
        method='fullRandom', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('tab_task_4.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(loop_L)  # add the loop to the experiment
    thisLoop_L = loop_L.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_L.rgb)
    if thisLoop_L != None:
        for paramName in thisLoop_L:
            globals()[paramName] = thisLoop_L[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop_L in loop_L:
        loop_L.status = STARTED
        if hasattr(thisLoop_L, 'status'):
            thisLoop_L.status = STARTED
        currentLoop = loop_L
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_L.rgb)
        if thisLoop_L != None:
            for paramName in thisLoop_L:
                globals()[paramName] = thisLoop_L[paramName]
        
        # --- Prepare to start Routine "task_L" ---
        # create an object to store info about Routine task_L
        task_L = data.Routine(
            name='task_L',
            components=[sq_1, sq_2, resp, text],
        )
        task_L.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        sq_1.setOpacity(op1)
        sq_1.setPos((xPos1, 0))
        sq_1.setSize((w1, w1))
        sq_1.setOri(or1)
        sq_2.setOpacity(op2)
        sq_2.setPos((xPos2, 0))
        sq_2.setSize((w2, w2))
        sq_2.setOri(or2)
        # create starting attributes for resp
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        # store start times for task_L
        task_L.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        task_L.tStart = globalClock.getTime(format='float')
        task_L.status = STARTED
        thisExp.addData('task_L.started', task_L.tStart)
        task_L.maxDuration = None
        # keep track of which components have finished
        task_LComponents = task_L.components
        for thisComponent in task_L.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "task_L" ---
        task_L.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_L, 'status') and thisLoop_L.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *sq_1* updates
            
            # if sq_1 is starting this frame...
            if sq_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sq_1.frameNStart = frameN  # exact frame index
                sq_1.tStart = t  # local t and not account for scr refresh
                sq_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sq_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                sq_1.status = STARTED
                sq_1.setAutoDraw(True)
            
            # if sq_1 is active this frame...
            if sq_1.status == STARTED:
                # update params
                pass
            
            # if sq_1 is stopping this frame...
            if sq_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sq_1.tStartRefresh + time-frameTolerance:
                    # keep track of stop time/frame for later
                    sq_1.tStop = t  # not accounting for scr refresh
                    sq_1.tStopRefresh = tThisFlipGlobal  # on global time
                    sq_1.frameNStop = frameN  # exact frame index
                    # update status
                    sq_1.status = FINISHED
                    sq_1.setAutoDraw(False)
            
            # *sq_2* updates
            
            # if sq_2 is starting this frame...
            if sq_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sq_2.frameNStart = frameN  # exact frame index
                sq_2.tStart = t  # local t and not account for scr refresh
                sq_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sq_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                sq_2.status = STARTED
                sq_2.setAutoDraw(True)
            
            # if sq_2 is active this frame...
            if sq_2.status == STARTED:
                # update params
                pass
            
            # if sq_2 is stopping this frame...
            if sq_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sq_2.tStartRefresh + time-frameTolerance:
                    # keep track of stop time/frame for later
                    sq_2.tStop = t  # not accounting for scr refresh
                    sq_2.tStopRefresh = tThisFlipGlobal  # on global time
                    sq_2.frameNStop = frameN  # exact frame index
                    # update status
                    sq_2.status = FINISHED
                    sq_2.setAutoDraw(False)
            
            # *resp* updates
            waitOnFlip = False
            
            # if resp is starting this frame...
            if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'resp.started')
                # update status
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            
            # if resp is stopping this frame...
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + time-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.tStopRefresh = tThisFlipGlobal  # on global time
                    resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'resp.stopped')
                    # update status
                    resp.status = FINISHED
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['right','left'], ignoreKeys=["escape"], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    resp.duration = _resp_allKeys[-1].duration
                    # was this correct?
                    if (resp.keys == str(corr_answ)) or (resp.keys == corr_answ):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + time-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=task_L,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                task_L.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in task_L.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task_L" ---
        for thisComponent in task_L.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for task_L
        task_L.tStop = globalClock.getTime(format='float')
        task_L.tStopRefresh = tThisFlipGlobal
        thisExp.addData('task_L.stopped', task_L.tStop)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(corr_answ).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for loop_L (TrialHandler)
        loop_L.addData('resp.keys',resp.keys)
        loop_L.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            loop_L.addData('resp.rt', resp.rt)
            loop_L.addData('resp.duration', resp.duration)
        # the Routine "task_L" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fb_task" ---
        # create an object to store info about Routine fb_task
        fb_task = data.Routine(
            name='fb_task',
            components=[text_fb_task],
        )
        fb_task.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_4
        if resp.keys:
           all_rt.append(resp.rt)
           if resp.corr == 1:
               msg = 'Верно!'
               corr_sum +=1
           else:
               msg = 'Увы('
        else:
            msg = 'Не успели'
            
        
        
        text_fb_task.setText(msg)
        # store start times for fb_task
        fb_task.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fb_task.tStart = globalClock.getTime(format='float')
        fb_task.status = STARTED
        thisExp.addData('fb_task.started', fb_task.tStart)
        fb_task.maxDuration = None
        # keep track of which components have finished
        fb_taskComponents = fb_task.components
        for thisComponent in fb_task.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fb_task" ---
        fb_task.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_L, 'status') and thisLoop_L.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_fb_task* updates
            
            # if text_fb_task is starting this frame...
            if text_fb_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_fb_task.frameNStart = frameN  # exact frame index
                text_fb_task.tStart = t  # local t and not account for scr refresh
                text_fb_task.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fb_task, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_fb_task.status = STARTED
                text_fb_task.setAutoDraw(True)
            
            # if text_fb_task is active this frame...
            if text_fb_task.status == STARTED:
                # update params
                pass
            
            # if text_fb_task is stopping this frame...
            if text_fb_task.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_fb_task.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    text_fb_task.tStop = t  # not accounting for scr refresh
                    text_fb_task.tStopRefresh = tThisFlipGlobal  # on global time
                    text_fb_task.frameNStop = frameN  # exact frame index
                    # update status
                    text_fb_task.status = FINISHED
                    text_fb_task.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=fb_task,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fb_task.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fb_task.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fb_task" ---
        for thisComponent in fb_task.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fb_task
        fb_task.tStop = globalClock.getTime(format='float')
        fb_task.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fb_task.stopped', fb_task.tStop)
        # Run 'End Routine' code from code_4
        mean_rt = sum(all_rt) / len(all_rt)
        tmp = 0.0
        for x in all_rt:
            tmp += (x - mean_rt) ** 2
        variance = tmp / len(all_rt)
        sd_rt = variance ** 0.5
        
        thisExp.addData('corr_sum', corr_sum)
        
        thisExp.addData('mean_rt', mean_rt)
        thisExp.addData('sd_rt', sd_rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fb_task.maxDurationReached:
            routineTimer.addTime(-fb_task.maxDuration)
        elif fb_task.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        # mark thisLoop_L as finished
        if hasattr(thisLoop_L, 'status'):
            thisLoop_L.status = FINISHED
        # if awaiting a pause, pause now
        if loop_L.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            loop_L.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'loop_L'
    loop_L.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    l_slid = data.TrialHandler2(
        name='l_slid',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('tabl_sl.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(l_slid)  # add the loop to the experiment
    thisL_slid = l_slid.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisL_slid.rgb)
    if thisL_slid != None:
        for paramName in thisL_slid:
            globals()[paramName] = thisL_slid[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisL_slid in l_slid:
        l_slid.status = STARTED
        if hasattr(thisL_slid, 'status'):
            thisL_slid.status = STARTED
        currentLoop = l_slid
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisL_slid.rgb)
        if thisL_slid != None:
            for paramName in thisL_slid:
                globals()[paramName] = thisL_slid[paramName]
        
        # --- Prepare to start Routine "slider" ---
        # create an object to store info about Routine slider
        slider = data.Routine(
            name='slider',
            components=[sl_h, text_sl],
        )
        slider.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        sl_h.reset()
        text_sl.setText(q_sl)
        # store start times for slider
        slider.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        slider.tStart = globalClock.getTime(format='float')
        slider.status = STARTED
        thisExp.addData('slider.started', slider.tStart)
        slider.maxDuration = None
        # keep track of which components have finished
        sliderComponents = slider.components
        for thisComponent in slider.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "slider" ---
        slider.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisL_slid, 'status') and thisL_slid.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *sl_h* updates
            
            # if sl_h is starting this frame...
            if sl_h.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sl_h.frameNStart = frameN  # exact frame index
                sl_h.tStart = t  # local t and not account for scr refresh
                sl_h.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sl_h, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sl_h.started')
                # update status
                sl_h.status = STARTED
                sl_h.setAutoDraw(True)
            
            # if sl_h is active this frame...
            if sl_h.status == STARTED:
                # update params
                pass
            
            # Check sl_h for response to end Routine
            if sl_h.getRating() is not None and sl_h.status == STARTED:
                continueRoutine = False
            
            # *text_sl* updates
            
            # if text_sl is starting this frame...
            if text_sl.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_sl.frameNStart = frameN  # exact frame index
                text_sl.tStart = t  # local t and not account for scr refresh
                text_sl.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_sl, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_sl.started')
                # update status
                text_sl.status = STARTED
                text_sl.setAutoDraw(True)
            
            # if text_sl is active this frame...
            if text_sl.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=slider,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                slider.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in slider.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "slider" ---
        for thisComponent in slider.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for slider
        slider.tStop = globalClock.getTime(format='float')
        slider.tStopRefresh = tThisFlipGlobal
        thisExp.addData('slider.stopped', slider.tStop)
        l_slid.addData('sl_h.response', sl_h.getRating())
        l_slid.addData('sl_h.rt', sl_h.getRT())
        l_slid.addData('sl_h.history', sl_h.getHistory())
        # the Routine "slider" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisL_slid as finished
        if hasattr(thisL_slid, 'status'):
            thisL_slid.status = FINISHED
        # if awaiting a pause, pause now
        if l_slid.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            l_slid.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'l_slid'
    l_slid.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "fin_sum" ---
    # create an object to store info about Routine fin_sum
    fin_sum = data.Routine(
        name='fin_sum',
        components=[text_5, key_resp_2],
    )
    fin_sum.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    
    final_sum = 'Всего правильных ответов:%s'%(corr_sum)
    text_5.setText(final_sum )
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # store start times for fin_sum
    fin_sum.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    fin_sum.tStart = globalClock.getTime(format='float')
    fin_sum.status = STARTED
    thisExp.addData('fin_sum.started', fin_sum.tStart)
    fin_sum.maxDuration = None
    # keep track of which components have finished
    fin_sumComponents = fin_sum.components
    for thisComponent in fin_sum.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fin_sum" ---
    fin_sum.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # if text_5 is stopping this frame...
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1.3-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.tStopRefresh = tThisFlipGlobal  # on global time
                text_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.stopped')
                # update status
                text_5.status = FINISHED
                text_5.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_2 is stopping this frame...
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 1.3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.tStopRefresh = tThisFlipGlobal  # on global time
                key_resp_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.stopped')
                # update status
                key_resp_2.status = FINISHED
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=fin_sum,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            fin_sum.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fin_sum.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fin_sum" ---
    for thisComponent in fin_sum.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for fin_sum
    fin_sum.tStop = globalClock.getTime(format='float')
    fin_sum.tStopRefresh = tThisFlipGlobal
    thisExp.addData('fin_sum.stopped', fin_sum.tStop)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if fin_sum.maxDurationReached:
        routineTimer.addTime(-fin_sum.maxDuration)
    elif fin_sum.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.300000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "Get_points" ---
    # create an object to store info about Routine Get_points
    Get_points = data.Routine(
        name='Get_points',
        components=[textbox, gp_key_resp],
    )
    Get_points.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    textbox.reset()
    # create starting attributes for gp_key_resp
    gp_key_resp.keys = []
    gp_key_resp.rt = []
    _gp_key_resp_allKeys = []
    # store start times for Get_points
    Get_points.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Get_points.tStart = globalClock.getTime(format='float')
    Get_points.status = STARTED
    thisExp.addData('Get_points.started', Get_points.tStart)
    Get_points.maxDuration = None
    # keep track of which components have finished
    Get_pointsComponents = Get_points.components
    for thisComponent in Get_points.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Get_points" ---
    Get_points.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox* updates
        
        # if textbox is starting this frame...
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox.started')
            # update status
            textbox.status = STARTED
            textbox.setAutoDraw(True)
        
        # if textbox is active this frame...
        if textbox.status == STARTED:
            # update params
            pass
        
        # *gp_key_resp* updates
        waitOnFlip = False
        
        # if gp_key_resp is starting this frame...
        if gp_key_resp.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            gp_key_resp.frameNStart = frameN  # exact frame index
            gp_key_resp.tStart = t  # local t and not account for scr refresh
            gp_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gp_key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            gp_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(gp_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(gp_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if gp_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = gp_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _gp_key_resp_allKeys.extend(theseKeys)
            if len(_gp_key_resp_allKeys):
                gp_key_resp.keys = _gp_key_resp_allKeys[-1].name  # just the last key pressed
                gp_key_resp.rt = _gp_key_resp_allKeys[-1].rt
                gp_key_resp.duration = _gp_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Get_points,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Get_points.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Get_points.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Get_points" ---
    for thisComponent in Get_points.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Get_points
    Get_points.tStop = globalClock.getTime(format='float')
    Get_points.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Get_points.stopped', Get_points.tStop)
    thisExp.addData('textbox.text',textbox.text)
    thisExp.nextEntry()
    # the Routine "Get_points" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "thanks" ---
    # create an object to store info about Routine thanks
    thanks = data.Routine(
        name='thanks',
        components=[text_th],
    )
    thanks.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for thanks
    thanks.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    thanks.tStart = globalClock.getTime(format='float')
    thanks.status = STARTED
    thisExp.addData('thanks.started', thanks.tStart)
    thanks.maxDuration = None
    # keep track of which components have finished
    thanksComponents = thanks.components
    for thisComponent in thanks.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "thanks" ---
    thanks.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_th* updates
        
        # if text_th is starting this frame...
        if text_th.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_th.frameNStart = frameN  # exact frame index
            text_th.tStart = t  # local t and not account for scr refresh
            text_th.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_th, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_th.started')
            # update status
            text_th.status = STARTED
            text_th.setAutoDraw(True)
        
        # if text_th is active this frame...
        if text_th.status == STARTED:
            # update params
            pass
        
        # if text_th is stopping this frame...
        if text_th.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_th.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_th.tStop = t  # not accounting for scr refresh
                text_th.tStopRefresh = tThisFlipGlobal  # on global time
                text_th.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_th.stopped')
                # update status
                text_th.status = FINISHED
                text_th.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=thanks,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            thanks.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thanks.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thanks" ---
    for thisComponent in thanks.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for thanks
    thanks.tStop = globalClock.getTime(format='float')
    thanks.tStopRefresh = tThisFlipGlobal
    thisExp.addData('thanks.stopped', thanks.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if thanks.maxDurationReached:
        routineTimer.addTime(-thanks.maxDuration)
    elif thanks.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
