/********************* 
 * 4_Calibr_Sum *
 *********************/


// store info about the experiment session:
let expName = '4_calibr_sum';  // from the Builder filename that created this script
let expInfo = {
    'name ': '',
    'gender ': '',
    'ag': '',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 0.2314), (- 0.2314), (- 0.2314)]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Main_instrRoutineBegin());
flowScheduler.add(Main_instrRoutineEachFrame());
flowScheduler.add(Main_instrRoutineEnd());
flowScheduler.add(instr_BJWRoutineBegin());
flowScheduler.add(instr_BJWRoutineEachFrame());
flowScheduler.add(instr_BJWRoutineEnd());
const BJW_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(BJW_trialsLoopBegin(BJW_trialsLoopScheduler));
flowScheduler.add(BJW_trialsLoopScheduler);
flowScheduler.add(BJW_trialsLoopEnd);


flowScheduler.add(instrRoutineBegin());
flowScheduler.add(instrRoutineEachFrame());
flowScheduler.add(instrRoutineEnd());
flowScheduler.add(instr_2RoutineBegin());
flowScheduler.add(instr_2RoutineEachFrame());
flowScheduler.add(instr_2RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);



flowScheduler.add(instr3RoutineBegin());
flowScheduler.add(instr3RoutineEachFrame());
flowScheduler.add(instr3RoutineEnd());
const loop_LLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loop_LLoopBegin(loop_LLoopScheduler));
flowScheduler.add(loop_LLoopScheduler);
flowScheduler.add(loop_LLoopEnd);



const l_slidLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(l_slidLoopBegin(l_slidLoopScheduler));
flowScheduler.add(l_slidLoopScheduler);
flowScheduler.add(l_slidLoopEnd);


flowScheduler.add(fin_sumRoutineBegin());
flowScheduler.add(fin_sumRoutineEachFrame());
flowScheduler.add(fin_sumRoutineEnd());
flowScheduler.add(Get_pointsRoutineBegin());
flowScheduler.add(Get_pointsRoutineEachFrame());
flowScheduler.add(Get_pointsRoutineEnd());
flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(send_experiment_to_osfRoutineBegin());
flowScheduler.add(send_experiment_to_osfRoutineEachFrame());
flowScheduler.add(send_experiment_to_osfRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'BJW.xlsx', 'path': 'BJW.xlsx'},
    {'name': 'trening2.xlsx', 'path': 'trening2.xlsx'},
    {'name': 'task_m_s4.xlsx', 'path': 'task_m_s4.xlsx'},
    {'name': 'tabl_sl.xlsx', 'path': 'tabl_sl.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["name"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var Main_instrClock;
var main_instr_text;
var main_instr_key;
var instr_BJWClock;
var BJW_inst_text;
var BJW_key_resp;
var BJWClock;
var BJW_slider;
var BJW_text;
var instrClock;
var text_instr;
var resp_instr;
var instr_2Clock;
var text_3;
var key_resp;
var trenClock;
var pol_1;
var pol_2;
var resp_tren;
var text_tren;
var fb_trenClock;
var msg;
var text_fb_tren;
var instr3Clock;
var text_4;
var reesp_instr;
var task_LClock;
var sq_1;
var sq_2;
var resp;
var text;
var fb_taskClock;
var corr_sum;
var all_rt;
var SD_rt;
var np;
var text_fb_task;
var sliderClock;
var sl_h;
var text_sl;
var fin_sumClock;
var final_sum;
var mean_rt;
var text_5;
var key_resp_2;
var Get_pointsClock;
var text_6;
var textbox;
var gp_key_resp;
var thanksClock;
var text_th;
var send_experiment_to_osfClock;
var text_7;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Main_instr"
  Main_instrClock = new util.Clock();
  main_instr_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'main_instr_text',
    text: 'Добрый день! Приглашаем принять участие в эксперименте и спасти одну магистерскую жизнь!\n\nСтуденты РАНХиГС, которые хотят получить баллы за участие, смогут оставить сведения о себе (номер строки) в конце эксперимента. \n\nЭксперимент запускается только на пк/ноутбуке. \n\nДля того, чтобы начать, нажмите на пробел',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  main_instr_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instr_BJW"
  instr_BJWClock = new util.Clock();
  BJW_inst_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'BJW_inst_text',
    text: 'Вам будут предложены утверждения (13). \n\nПожалуйста, оцените, насколько каждое утверждение соответствует вашему мнению. \n\nДля этого перетащите красный кружок мышкой на ту позицию шкалы, которая лучше всего отражает ваше отношение.\n\nМы исследуем мир и себя в нем. Пожалуйста, отвечайте честно и вдумчиво.\n\nНажмите "пробел", чтобы приступить.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  BJW_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "BJW"
  BJWClock = new util.Clock();
  BJW_slider = new visual.Slider({
    win: psychoJS.window, name: 'BJW_slider',
    startValue: 3,
    size: [1.0, 0.1], pos: [0, (- 0.4)], ori: 0.0, units: psychoJS.window.units,
    labels: ["\u0421\u043e\u0432\u0435\u0440\u0448\u0435\u043d\u043d\u043e \u043d\u0435 \u0441\u043e\u0433\u043b\u0430\u0441\u0435\u043d", "\u041d\u0435 \u0441\u043e\u0433\u043b\u0430\u0441\u0435\u043d", "\u0421\u043a\u043e\u0440\u0435\u0435 \u043d\u0435 \u0441\u043e\u0433\u043b\u0430\u0441\u0435\u043d", "\u0421\u043a\u043e\u0440\u0435\u0435 \u0441\u043e\u0433\u043b\u0430\u0441\u0435\u043d", "\u0421\u043e\u0433\u043b\u0430\u0441\u0435\u043d", "\u041f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e \u0441\u043e\u0433\u043b\u0430\u0441\u0435\u043d"], fontSize: 0.02, ticks: [1, 2, 3, 4, 5, 6],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: 0, 
    flip: true,
  });
  
  BJW_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'BJW_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  text_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_instr',
    text: 'Вам нужно будет сравнивать квадраты по размеру. \nЕсли больше правый квадрат, нажмите кнопку "вправо", еcли левый - то "влево".\n\nНажмите "пробел", чтобы приступить.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  resp_instr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instr_2"
  instr_2Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Сейчас тренировочный этап. \nВам нужно будет сравнивать квадраты по величине.\n\nЕсли больше правый квадрат, нажмите "вправо", если левый - то "влево".\nЕсли готовы - нажмите пробел и переходите к сравнению.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "tren"
  trenClock = new util.Clock();
  pol_1 = new visual.Rect ({
    win: psychoJS.window, name: 'pol_1', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 1.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: -1, 
    interpolate: true, 
  });
  
  pol_2 = new visual.Rect ({
    win: psychoJS.window, name: 'pol_2', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 1.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: -2, 
    interpolate: true, 
  });
  
  resp_tren = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_tren = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_tren',
    text: 'Если больше правый квадрат, нажмите "вправо", если левый - то "влево"',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "fb_tren"
  fb_trenClock = new util.Clock();
  // Run 'Begin Experiment' code from code_tr_2
  msg = "";
  
  text_fb_tren = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_fb_tren',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "instr3"
  instr3Clock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'А теперь - основной этап.  Но время  на выполнение  каждого задания будет ограничено. \nЕсли готовы - нажмите на пробел.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  reesp_instr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "task_L"
  task_LClock = new util.Clock();
  sq_1 = new visual.Rect ({
    win: psychoJS.window, name: 'sq_1', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 1.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color([1.0, 1.0, 1.0]), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: 0, 
    interpolate: true, 
  });
  
  sq_2 = new visual.Rect ({
    win: psychoJS.window, name: 'sq_2', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 1.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: -1, 
    interpolate: true, 
  });
  
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Если больше правый квадрат, нажмите "вправо", если левый - то "влево"',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "fb_task"
  fb_taskClock = new util.Clock();
  // Run 'Begin Experiment' code from code_4
  msg = "";
  corr_sum = 0;
  all_rt = [];
  SD_rt = [];
  np = null;
  
  text_fb_task = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_fb_task',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "slider"
  sliderClock = new util.Clock();
  sl_h = new visual.Slider({
    win: psychoJS.window, name: 'sl_h',
    startValue: 5,
    size: [1.0, 0.1], pos: [0, (- 0.4)], ori: 0.0, units: psychoJS.window.units,
    labels: ["\u0441\u043e\u0432\u0441\u0435\u043c \u043d\u0435\u0442", "\u043e\u0447\u0435\u043d\u044c"], fontSize: 0.03, ticks: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    granularity: 0.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: 0, 
    flip: true,
  });
  
  text_sl = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_sl',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "fin_sum"
  fin_sumClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  final_sum = "";
  mean_rt = 0;
  SD_rt = 0;
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Get_points"
  Get_pointsClock = new util.Clock();
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'Для студентов РАНХиГСа - введите номер строки для учета баллов, \nдля нестудентов - 2 любые буквы \nи нажмите на пробел для завершения.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox',
    text: '',
    placeholder: undefined,
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'bottom-center',
    depth: -1.0 
  });
  
  gp_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  text_th = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_th',
    text: 'Спасибо за участие!\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "send_experiment_to_osf"
  send_experiment_to_osfClock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'Сохраняем данные',
    font: 'Arial',
    units: undefined, 
    pos: [0, 1], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var Main_instrMaxDurationReached;
var _main_instr_key_allKeys;
var Main_instrMaxDuration;
var Main_instrComponents;
function Main_instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Main_instr' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    Main_instrClock.reset();
    routineTimer.reset();
    Main_instrMaxDurationReached = false;
    // update component parameters for each repeat
    main_instr_key.keys = undefined;
    main_instr_key.rt = undefined;
    _main_instr_key_allKeys = [];
    psychoJS.experiment.addData('Main_instr.started', globalClock.getTime());
    Main_instrMaxDuration = null
    // keep track of which components have finished
    Main_instrComponents = [];
    Main_instrComponents.push(main_instr_text);
    Main_instrComponents.push(main_instr_key);
    
    Main_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Main_instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Main_instr' ---
    // get current time
    t = Main_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *main_instr_text* updates
    if (t >= 0.0 && main_instr_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      main_instr_text.tStart = t;  // (not accounting for frame time here)
      main_instr_text.frameNStart = frameN;  // exact frame index
      
      main_instr_text.setAutoDraw(true);
    }
    
    
    // if main_instr_text is active this frame...
    if (main_instr_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *main_instr_key* updates
    if (t >= 0.0 && main_instr_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      main_instr_key.tStart = t;  // (not accounting for frame time here)
      main_instr_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { main_instr_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { main_instr_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { main_instr_key.clearEvents(); });
    }
    
    // if main_instr_key is active this frame...
    if (main_instr_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = main_instr_key.getKeys({keyList: 'space', waitRelease: false});
      _main_instr_key_allKeys = _main_instr_key_allKeys.concat(theseKeys);
      if (_main_instr_key_allKeys.length > 0) {
        main_instr_key.keys = _main_instr_key_allKeys[_main_instr_key_allKeys.length - 1].name;  // just the last key pressed
        main_instr_key.rt = _main_instr_key_allKeys[_main_instr_key_allKeys.length - 1].rt;
        main_instr_key.duration = _main_instr_key_allKeys[_main_instr_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Main_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Main_instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Main_instr' ---
    Main_instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Main_instr.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(main_instr_key.corr, level);
    }
    psychoJS.experiment.addData('main_instr_key.keys', main_instr_key.keys);
    if (typeof main_instr_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('main_instr_key.rt', main_instr_key.rt);
        psychoJS.experiment.addData('main_instr_key.duration', main_instr_key.duration);
        routineTimer.reset();
        }
    
    main_instr_key.stop();
    // the Routine "Main_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instr_BJWMaxDurationReached;
var _BJW_key_resp_allKeys;
var instr_BJWMaxDuration;
var instr_BJWComponents;
function instr_BJWRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr_BJW' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instr_BJWClock.reset();
    routineTimer.reset();
    instr_BJWMaxDurationReached = false;
    // update component parameters for each repeat
    BJW_key_resp.keys = undefined;
    BJW_key_resp.rt = undefined;
    _BJW_key_resp_allKeys = [];
    psychoJS.experiment.addData('instr_BJW.started', globalClock.getTime());
    instr_BJWMaxDuration = null
    // keep track of which components have finished
    instr_BJWComponents = [];
    instr_BJWComponents.push(BJW_inst_text);
    instr_BJWComponents.push(BJW_key_resp);
    
    instr_BJWComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instr_BJWRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr_BJW' ---
    // get current time
    t = instr_BJWClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *BJW_inst_text* updates
    if (t >= 0.0 && BJW_inst_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BJW_inst_text.tStart = t;  // (not accounting for frame time here)
      BJW_inst_text.frameNStart = frameN;  // exact frame index
      
      BJW_inst_text.setAutoDraw(true);
    }
    
    
    // if BJW_inst_text is active this frame...
    if (BJW_inst_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *BJW_key_resp* updates
    if (t >= 0.0 && BJW_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BJW_key_resp.tStart = t;  // (not accounting for frame time here)
      BJW_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { BJW_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { BJW_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { BJW_key_resp.clearEvents(); });
    }
    
    // if BJW_key_resp is active this frame...
    if (BJW_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = BJW_key_resp.getKeys({keyList: 'space', waitRelease: false});
      _BJW_key_resp_allKeys = _BJW_key_resp_allKeys.concat(theseKeys);
      if (_BJW_key_resp_allKeys.length > 0) {
        BJW_key_resp.keys = _BJW_key_resp_allKeys[_BJW_key_resp_allKeys.length - 1].name;  // just the last key pressed
        BJW_key_resp.rt = _BJW_key_resp_allKeys[_BJW_key_resp_allKeys.length - 1].rt;
        BJW_key_resp.duration = _BJW_key_resp_allKeys[_BJW_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_BJWComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_BJWRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr_BJW' ---
    instr_BJWComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instr_BJW.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(BJW_key_resp.corr, level);
    }
    psychoJS.experiment.addData('BJW_key_resp.keys', BJW_key_resp.keys);
    if (typeof BJW_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('BJW_key_resp.rt', BJW_key_resp.rt);
        psychoJS.experiment.addData('BJW_key_resp.duration', BJW_key_resp.duration);
        routineTimer.reset();
        }
    
    BJW_key_resp.stop();
    // the Routine "instr_BJW" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var BJW_trials;
function BJW_trialsLoopBegin(BJW_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    BJW_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'BJW.xlsx',
      seed: undefined, name: 'BJW_trials'
    });
    psychoJS.experiment.addLoop(BJW_trials); // add the loop to the experiment
    currentLoop = BJW_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    BJW_trials.forEach(function() {
      snapshot = BJW_trials.getSnapshot();
    
      BJW_trialsLoopScheduler.add(importConditions(snapshot));
      BJW_trialsLoopScheduler.add(BJWRoutineBegin(snapshot));
      BJW_trialsLoopScheduler.add(BJWRoutineEachFrame());
      BJW_trialsLoopScheduler.add(BJWRoutineEnd(snapshot));
      BJW_trialsLoopScheduler.add(BJW_trialsLoopEndIteration(BJW_trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function BJW_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(BJW_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function BJW_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'trening2.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trenRoutineBegin(snapshot));
      trialsLoopScheduler.add(trenRoutineEachFrame());
      trialsLoopScheduler.add(trenRoutineEnd(snapshot));
      trialsLoopScheduler.add(fb_trenRoutineBegin(snapshot));
      trialsLoopScheduler.add(fb_trenRoutineEachFrame());
      trialsLoopScheduler.add(fb_trenRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var loop_L;
function loop_LLoopBegin(loop_LLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_L = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'task_m_s4.xlsx',
      seed: undefined, name: 'loop_L'
    });
    psychoJS.experiment.addLoop(loop_L); // add the loop to the experiment
    currentLoop = loop_L;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_L.forEach(function() {
      snapshot = loop_L.getSnapshot();
    
      loop_LLoopScheduler.add(importConditions(snapshot));
      loop_LLoopScheduler.add(task_LRoutineBegin(snapshot));
      loop_LLoopScheduler.add(task_LRoutineEachFrame());
      loop_LLoopScheduler.add(task_LRoutineEnd(snapshot));
      loop_LLoopScheduler.add(fb_taskRoutineBegin(snapshot));
      loop_LLoopScheduler.add(fb_taskRoutineEachFrame());
      loop_LLoopScheduler.add(fb_taskRoutineEnd(snapshot));
      loop_LLoopScheduler.add(loop_LLoopEndIteration(loop_LLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function loop_LLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_L);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop_LLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var l_slid;
function l_slidLoopBegin(l_slidLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    l_slid = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'tabl_sl.xlsx',
      seed: undefined, name: 'l_slid'
    });
    psychoJS.experiment.addLoop(l_slid); // add the loop to the experiment
    currentLoop = l_slid;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    l_slid.forEach(function() {
      snapshot = l_slid.getSnapshot();
    
      l_slidLoopScheduler.add(importConditions(snapshot));
      l_slidLoopScheduler.add(sliderRoutineBegin(snapshot));
      l_slidLoopScheduler.add(sliderRoutineEachFrame());
      l_slidLoopScheduler.add(sliderRoutineEnd(snapshot));
      l_slidLoopScheduler.add(l_slidLoopEndIteration(l_slidLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function l_slidLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(l_slid);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function l_slidLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var BJWMaxDurationReached;
var BJWMaxDuration;
var BJWComponents;
function BJWRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'BJW' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    BJWClock.reset();
    routineTimer.reset();
    BJWMaxDurationReached = false;
    // update component parameters for each repeat
    BJW_slider.reset()
    BJW_text.setText(Text);
    psychoJS.experiment.addData('BJW.started', globalClock.getTime());
    BJWMaxDuration = null
    // keep track of which components have finished
    BJWComponents = [];
    BJWComponents.push(BJW_slider);
    BJWComponents.push(BJW_text);
    
    BJWComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function BJWRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'BJW' ---
    // get current time
    t = BJWClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *BJW_slider* updates
    if (t >= 0.0 && BJW_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BJW_slider.tStart = t;  // (not accounting for frame time here)
      BJW_slider.frameNStart = frameN;  // exact frame index
      
      BJW_slider.setAutoDraw(true);
    }
    
    
    // if BJW_slider is active this frame...
    if (BJW_slider.status === PsychoJS.Status.STARTED) {
    }
    
    
    // Check BJW_slider for response to end Routine
    if (BJW_slider.getRating() !== undefined && BJW_slider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    
    // *BJW_text* updates
    if (t >= 0.0 && BJW_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BJW_text.tStart = t;  // (not accounting for frame time here)
      BJW_text.frameNStart = frameN;  // exact frame index
      
      BJW_text.setAutoDraw(true);
    }
    
    
    // if BJW_text is active this frame...
    if (BJW_text.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    BJWComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function BJWRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'BJW' ---
    BJWComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('BJW.stopped', globalClock.getTime());
    psychoJS.experiment.addData('BJW_slider.response', BJW_slider.getRating());
    psychoJS.experiment.addData('BJW_slider.rt', BJW_slider.getRT());
    psychoJS.experiment.addData('BJW_slider.history', BJW_slider.getHistory());
    // the Routine "BJW" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instrMaxDurationReached;
var _resp_instr_allKeys;
var instrMaxDuration;
var instrComponents;
function instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instrClock.reset();
    routineTimer.reset();
    instrMaxDurationReached = false;
    // update component parameters for each repeat
    resp_instr.keys = undefined;
    resp_instr.rt = undefined;
    _resp_instr_allKeys = [];
    psychoJS.experiment.addData('instr.started', globalClock.getTime());
    instrMaxDuration = null
    // keep track of which components have finished
    instrComponents = [];
    instrComponents.push(text_instr);
    instrComponents.push(resp_instr);
    
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr' ---
    // get current time
    t = instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_instr* updates
    if (t >= 0.0 && text_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_instr.tStart = t;  // (not accounting for frame time here)
      text_instr.frameNStart = frameN;  // exact frame index
      
      text_instr.setAutoDraw(true);
    }
    
    
    // if text_instr is active this frame...
    if (text_instr.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *resp_instr* updates
    if (t >= 0.0 && resp_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_instr.tStart = t;  // (not accounting for frame time here)
      resp_instr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      resp_instr.clock.reset();
      resp_instr.start();
    }
    
    // if resp_instr is active this frame...
    if (resp_instr.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_instr.getKeys({keyList: [], waitRelease: false});
      _resp_instr_allKeys = _resp_instr_allKeys.concat(theseKeys);
      if (_resp_instr_allKeys.length > 0) {
        resp_instr.keys = _resp_instr_allKeys[_resp_instr_allKeys.length - 1].name;  // just the last key pressed
        resp_instr.rt = _resp_instr_allKeys[_resp_instr_allKeys.length - 1].rt;
        resp_instr.duration = _resp_instr_allKeys[_resp_instr_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr' ---
    instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instr.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_instr.corr, level);
    }
    psychoJS.experiment.addData('resp_instr.keys', resp_instr.keys);
    if (typeof resp_instr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_instr.rt', resp_instr.rt);
        psychoJS.experiment.addData('resp_instr.duration', resp_instr.duration);
        routineTimer.reset();
        }
    
    resp_instr.stop();
    // the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instr_2MaxDurationReached;
var _key_resp_allKeys;
var instr_2MaxDuration;
var instr_2Components;
function instr_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instr_2Clock.reset();
    routineTimer.reset();
    instr_2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('instr_2.started', globalClock.getTime());
    instr_2MaxDuration = null
    // keep track of which components have finished
    instr_2Components = [];
    instr_2Components.push(text_3);
    instr_2Components.push(key_resp);
    
    instr_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instr_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr_2' ---
    // get current time
    t = instr_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    
    // if text_3 is active this frame...
    if (text_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    // if key_resp is active this frame...
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: 'space', waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr_2' ---
    instr_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instr_2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "instr_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trenMaxDurationReached;
var _resp_tren_allKeys;
var trenMaxDuration;
var trenComponents;
function trenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'tren' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trenClock.reset();
    routineTimer.reset();
    trenMaxDurationReached = false;
    // update component parameters for each repeat
    pol_1.setOpacity(op1);
    pol_1.setPos([xPos1, 0]);
    pol_1.setSize([w1, w1]);
    pol_1.setOri(or1);
    pol_2.setOpacity(op1);
    pol_2.setPos([xPos2, 0]);
    pol_2.setSize([w2, w2]);
    pol_2.setOri(or2);
    resp_tren.keys = undefined;
    resp_tren.rt = undefined;
    _resp_tren_allKeys = [];
    psychoJS.experiment.addData('tren.started', globalClock.getTime());
    trenMaxDuration = null
    // keep track of which components have finished
    trenComponents = [];
    trenComponents.push(pol_1);
    trenComponents.push(pol_2);
    trenComponents.push(resp_tren);
    trenComponents.push(text_tren);
    
    trenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'tren' ---
    // get current time
    t = trenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pol_1* updates
    if (t >= 0.0 && pol_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pol_1.tStart = t;  // (not accounting for frame time here)
      pol_1.frameNStart = frameN;  // exact frame index
      
      pol_1.setAutoDraw(true);
    }
    
    
    // if pol_1 is active this frame...
    if (pol_1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *pol_2* updates
    if (t >= 0.0 && pol_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pol_2.tStart = t;  // (not accounting for frame time here)
      pol_2.frameNStart = frameN;  // exact frame index
      
      pol_2.setAutoDraw(true);
    }
    
    
    // if pol_2 is active this frame...
    if (pol_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *resp_tren* updates
    if (t >= 0.0 && resp_tren.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_tren.tStart = t;  // (not accounting for frame time here)
      resp_tren.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      resp_tren.clock.reset();
      resp_tren.start();
    }
    
    // if resp_tren is active this frame...
    if (resp_tren.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_tren.getKeys({keyList: ['left','right'], waitRelease: false});
      _resp_tren_allKeys = _resp_tren_allKeys.concat(theseKeys);
      if (_resp_tren_allKeys.length > 0) {
        resp_tren.keys = _resp_tren_allKeys[_resp_tren_allKeys.length - 1].name;  // just the last key pressed
        resp_tren.rt = _resp_tren_allKeys[_resp_tren_allKeys.length - 1].rt;
        resp_tren.duration = _resp_tren_allKeys[_resp_tren_allKeys.length - 1].duration;
        // was this correct?
        if (resp_tren.keys == corr_answ) {
            resp_tren.corr = 1;
        } else {
            resp_tren.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_tren* updates
    if (t >= 0.0 && text_tren.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_tren.tStart = t;  // (not accounting for frame time here)
      text_tren.frameNStart = frameN;  // exact frame index
      
      text_tren.setAutoDraw(true);
    }
    
    
    // if text_tren is active this frame...
    if (text_tren.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'tren' ---
    trenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('tren.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (resp_tren.keys === undefined) {
      if (['None','none',undefined].includes(corr_answ)) {
         resp_tren.corr = 1;  // correct non-response
      } else {
         resp_tren.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_tren.corr, level);
    }
    psychoJS.experiment.addData('resp_tren.keys', resp_tren.keys);
    psychoJS.experiment.addData('resp_tren.corr', resp_tren.corr);
    if (typeof resp_tren.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_tren.rt', resp_tren.rt);
        psychoJS.experiment.addData('resp_tren.duration', resp_tren.duration);
        routineTimer.reset();
        }
    
    resp_tren.stop();
    // the Routine "tren" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fb_trenMaxDurationReached;
var fb_trenMaxDuration;
var fb_trenComponents;
function fb_trenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fb_tren' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    fb_trenClock.reset(routineTimer.getTime());
    routineTimer.add(0.500000);
    fb_trenMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_tr_2
    if ((resp_tren.corr === 1)) {
        msg = "\u0412\u0435\u0440\u043d\u043e!";
    } else {
        msg = "\u0423\u0432\u044b(";
    }
    
    text_fb_tren.setText(msg);
    psychoJS.experiment.addData('fb_tren.started', globalClock.getTime());
    fb_trenMaxDuration = null
    // keep track of which components have finished
    fb_trenComponents = [];
    fb_trenComponents.push(text_fb_tren);
    
    fb_trenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fb_trenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fb_tren' ---
    // get current time
    t = fb_trenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_fb_tren* updates
    if (t >= 0.0 && text_fb_tren.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_fb_tren.tStart = t;  // (not accounting for frame time here)
      text_fb_tren.frameNStart = frameN;  // exact frame index
      
      text_fb_tren.setAutoDraw(true);
    }
    
    
    // if text_fb_tren is active this frame...
    if (text_fb_tren.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_fb_tren.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_fb_tren.tStop = t;  // not accounting for scr refresh
      text_fb_tren.frameNStop = frameN;  // exact frame index
      // update status
      text_fb_tren.status = PsychoJS.Status.FINISHED;
      text_fb_tren.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fb_trenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fb_trenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fb_tren' ---
    fb_trenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('fb_tren.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (fb_trenMaxDurationReached) {
        fb_trenClock.add(fb_trenMaxDuration);
    } else {
        fb_trenClock.add(0.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instr3MaxDurationReached;
var _reesp_instr_allKeys;
var instr3MaxDuration;
var instr3Components;
function instr3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instr3Clock.reset();
    routineTimer.reset();
    instr3MaxDurationReached = false;
    // update component parameters for each repeat
    reesp_instr.keys = undefined;
    reesp_instr.rt = undefined;
    _reesp_instr_allKeys = [];
    psychoJS.experiment.addData('instr3.started', globalClock.getTime());
    instr3MaxDuration = null
    // keep track of which components have finished
    instr3Components = [];
    instr3Components.push(text_4);
    instr3Components.push(reesp_instr);
    
    instr3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instr3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr3' ---
    // get current time
    t = instr3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    
    // if text_4 is active this frame...
    if (text_4.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *reesp_instr* updates
    if (t >= 0.0 && reesp_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reesp_instr.tStart = t;  // (not accounting for frame time here)
      reesp_instr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      reesp_instr.clock.reset();
      reesp_instr.start();
    }
    
    // if reesp_instr is active this frame...
    if (reesp_instr.status === PsychoJS.Status.STARTED) {
      let theseKeys = reesp_instr.getKeys({keyList: 'space', waitRelease: false});
      _reesp_instr_allKeys = _reesp_instr_allKeys.concat(theseKeys);
      if (_reesp_instr_allKeys.length > 0) {
        reesp_instr.keys = _reesp_instr_allKeys[_reesp_instr_allKeys.length - 1].name;  // just the last key pressed
        reesp_instr.rt = _reesp_instr_allKeys[_reesp_instr_allKeys.length - 1].rt;
        reesp_instr.duration = _reesp_instr_allKeys[_reesp_instr_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr3' ---
    instr3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instr3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(reesp_instr.corr, level);
    }
    psychoJS.experiment.addData('reesp_instr.keys', reesp_instr.keys);
    if (typeof reesp_instr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('reesp_instr.rt', reesp_instr.rt);
        psychoJS.experiment.addData('reesp_instr.duration', reesp_instr.duration);
        routineTimer.reset();
        }
    
    reesp_instr.stop();
    // the Routine "instr3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var task_LMaxDurationReached;
var _resp_allKeys;
var task_LMaxDuration;
var task_LComponents;
function task_LRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'task_L' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    task_LClock.reset();
    routineTimer.reset();
    task_LMaxDurationReached = false;
    // update component parameters for each repeat
    sq_1.setOpacity(op1);
    sq_1.setPos([xPos1, 0]);
    sq_1.setSize([w1, w1]);
    sq_1.setOri(or1);
    sq_2.setOpacity(op2);
    sq_2.setPos([xPos2, 0]);
    sq_2.setSize([w2, w2]);
    sq_2.setOri(or2);
    resp.keys = undefined;
    resp.rt = undefined;
    _resp_allKeys = [];
    psychoJS.experiment.addData('task_L.started', globalClock.getTime());
    task_LMaxDuration = null
    // keep track of which components have finished
    task_LComponents = [];
    task_LComponents.push(sq_1);
    task_LComponents.push(sq_2);
    task_LComponents.push(resp);
    task_LComponents.push(text);
    
    task_LComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function task_LRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'task_L' ---
    // get current time
    t = task_LClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *sq_1* updates
    if (t >= 0.0 && sq_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sq_1.tStart = t;  // (not accounting for frame time here)
      sq_1.frameNStart = frameN;  // exact frame index
      
      sq_1.setAutoDraw(true);
    }
    
    
    // if sq_1 is active this frame...
    if (sq_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + time - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (sq_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      sq_1.tStop = t;  // not accounting for scr refresh
      sq_1.frameNStop = frameN;  // exact frame index
      // update status
      sq_1.status = PsychoJS.Status.FINISHED;
      sq_1.setAutoDraw(false);
    }
    
    
    // *sq_2* updates
    if (t >= 0.0 && sq_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sq_2.tStart = t;  // (not accounting for frame time here)
      sq_2.frameNStart = frameN;  // exact frame index
      
      sq_2.setAutoDraw(true);
    }
    
    
    // if sq_2 is active this frame...
    if (sq_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + time - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (sq_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      sq_2.tStop = t;  // not accounting for scr refresh
      sq_2.frameNStop = frameN;  // exact frame index
      // update status
      sq_2.status = PsychoJS.Status.FINISHED;
      sq_2.setAutoDraw(false);
    }
    
    
    // *resp* updates
    if (t >= 0.0 && resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp.tStart = t;  // (not accounting for frame time here)
      resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp.start(); }); // start on screen flip
    }
    frameRemains = 0.0 + time - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      resp.tStop = t;  // not accounting for scr refresh
      resp.frameNStop = frameN;  // exact frame index
      // update status
      resp.status = PsychoJS.Status.FINISHED;
      frameRemains = 0.0 + time - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        resp.tStop = t;  // not accounting for scr refresh
        resp.frameNStop = frameN;  // exact frame index
        // update status
        resp.status = PsychoJS.Status.FINISHED;
        resp.status = PsychoJS.Status.FINISHED;
          }
        
      }
      
      // if resp is active this frame...
      if (resp.status === PsychoJS.Status.STARTED) {
        let theseKeys = resp.getKeys({keyList: ['right','left'], waitRelease: false});
        _resp_allKeys = _resp_allKeys.concat(theseKeys);
        if (_resp_allKeys.length > 0) {
          resp.keys = _resp_allKeys[_resp_allKeys.length - 1].name;  // just the last key pressed
          resp.rt = _resp_allKeys[_resp_allKeys.length - 1].rt;
          resp.duration = _resp_allKeys[_resp_allKeys.length - 1].duration;
          // was this correct?
          if (resp.keys == corr_answ) {
              resp.corr = 1;
          } else {
              resp.corr = 0;
          }
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *text* updates
      if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        text.tStart = t;  // (not accounting for frame time here)
        text.frameNStart = frameN;  // exact frame index
        
        text.setAutoDraw(true);
      }
      
      
      // if text is active this frame...
      if (text.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + time - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        text.tStop = t;  // not accounting for scr refresh
        text.frameNStop = frameN;  // exact frame index
        // update status
        text.status = PsychoJS.Status.FINISHED;
        text.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      task_LComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function task_LRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'task_L' ---
      task_LComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('task_L.stopped', globalClock.getTime());
      // was no response the correct answer?!
      if (resp.keys === undefined) {
        if (['None','none',undefined].includes(corr_answ)) {
           resp.corr = 1;  // correct non-response
        } else {
           resp.corr = 0;  // failed to respond (incorrectly)
        }
      }
      // store data for current loop
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(resp.corr, level);
      }
      psychoJS.experiment.addData('resp.keys', resp.keys);
      psychoJS.experiment.addData('resp.corr', resp.corr);
      if (typeof resp.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('resp.rt', resp.rt);
          psychoJS.experiment.addData('resp.duration', resp.duration);
          routineTimer.reset();
          }
      
      resp.stop();
      // the Routine "task_L" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var fb_taskMaxDurationReached;
var fb_taskMaxDuration;
var fb_taskComponents;
function fb_taskRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'fb_task' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      fb_taskClock.reset(routineTimer.getTime());
      routineTimer.add(0.300000);
      fb_taskMaxDurationReached = false;
      // update component parameters for each repeat
      // Run 'Begin Routine' code from code_4
      if (resp.keys) {
          all_rt.push(resp.rt);
          if ((resp.corr === 1)) {
              msg = "\u0412\u0435\u0440\u043d\u043e!";
              corr_sum += 1;
          } else {
              msg = "\u0423\u0432\u044b(";
          }
      } else {
          msg = "\u041d\u0435 \u0443\u0441\u043f\u0435\u043b\u0438";
      }
      
      text_fb_task.setText(msg);
      psychoJS.experiment.addData('fb_task.started', globalClock.getTime());
      fb_taskMaxDuration = null
      // keep track of which components have finished
      fb_taskComponents = [];
      fb_taskComponents.push(text_fb_task);
      
      fb_taskComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function fb_taskRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'fb_task' ---
      // get current time
      t = fb_taskClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *text_fb_task* updates
      if (t >= 0.0 && text_fb_task.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        text_fb_task.tStart = t;  // (not accounting for frame time here)
        text_fb_task.frameNStart = frameN;  // exact frame index
        
        text_fb_task.setAutoDraw(true);
      }
      
      
      // if text_fb_task is active this frame...
      if (text_fb_task.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (text_fb_task.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        text_fb_task.tStop = t;  // not accounting for scr refresh
        text_fb_task.frameNStop = frameN;  // exact frame index
        // update status
        text_fb_task.status = PsychoJS.Status.FINISHED;
        text_fb_task.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      fb_taskComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
var tmp;
var variance;
var sd_rt;
function fb_taskRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'fb_task' ---
      fb_taskComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('fb_task.stopped', globalClock.getTime());
      // Run 'End Routine' code from code_4
      mean_rt = (util.sum(all_rt) / all_rt.length);
      tmp = 0.0;
      for (var x, _pj_c = 0, _pj_a = all_rt, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
          x = _pj_a[_pj_c];
          tmp += Math.pow((x - mean_rt), 2);
      }
      variance = (tmp / all_rt.length);
      sd_rt = Math.pow(variance, 0.5);
      psychoJS.experiment.addData("corr_sum", corr_sum);
      psychoJS.experiment.addData("mean_rt", mean_rt);
      psychoJS.experiment.addData("sd_rt", sd_rt);
      
      if (routineForceEnded) {
          routineTimer.reset();} else if (fb_taskMaxDurationReached) {
          fb_taskClock.add(fb_taskMaxDuration);
      } else {
          fb_taskClock.add(0.300000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var sliderMaxDurationReached;
var sliderMaxDuration;
var sliderComponents;
function sliderRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'slider' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      sliderClock.reset();
      routineTimer.reset();
      sliderMaxDurationReached = false;
      // update component parameters for each repeat
      sl_h.reset()
      text_sl.setText(q_sl);
      psychoJS.experiment.addData('slider.started', globalClock.getTime());
      sliderMaxDuration = null
      // keep track of which components have finished
      sliderComponents = [];
      sliderComponents.push(sl_h);
      sliderComponents.push(text_sl);
      
      sliderComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function sliderRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'slider' ---
      // get current time
      t = sliderClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *sl_h* updates
      if (t >= 0.0 && sl_h.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        sl_h.tStart = t;  // (not accounting for frame time here)
        sl_h.frameNStart = frameN;  // exact frame index
        
        sl_h.setAutoDraw(true);
      }
      
      
      // if sl_h is active this frame...
      if (sl_h.status === PsychoJS.Status.STARTED) {
      }
      
      
      // Check sl_h for response to end Routine
      if (sl_h.getRating() !== undefined && sl_h.status === PsychoJS.Status.STARTED) {
        continueRoutine = false; }
      
      // *text_sl* updates
      if (t >= 0.0 && text_sl.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        text_sl.tStart = t;  // (not accounting for frame time here)
        text_sl.frameNStart = frameN;  // exact frame index
        
        text_sl.setAutoDraw(true);
      }
      
      
      // if text_sl is active this frame...
      if (text_sl.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      sliderComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function sliderRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'slider' ---
      sliderComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('slider.stopped', globalClock.getTime());
      psychoJS.experiment.addData('sl_h.response', sl_h.getRating());
      psychoJS.experiment.addData('sl_h.rt', sl_h.getRT());
      psychoJS.experiment.addData('sl_h.history', sl_h.getHistory());
      // the Routine "slider" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var fin_sumMaxDurationReached;
var _key_resp_2_allKeys;
var fin_sumMaxDuration;
var fin_sumComponents;
function fin_sumRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'fin_sum' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      fin_sumClock.reset(routineTimer.getTime());
      routineTimer.add(1.300000);
      fin_sumMaxDurationReached = false;
      // update component parameters for each repeat
      // Run 'Begin Routine' code from code
      final_sum = `Всего правильных ответов:${corr_sum}`;
      
      text_5.setText(final_sum);
      key_resp_2.keys = undefined;
      key_resp_2.rt = undefined;
      _key_resp_2_allKeys = [];
      psychoJS.experiment.addData('fin_sum.started', globalClock.getTime());
      fin_sumMaxDuration = null
      // keep track of which components have finished
      fin_sumComponents = [];
      fin_sumComponents.push(text_5);
      fin_sumComponents.push(key_resp_2);
      
      fin_sumComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function fin_sumRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'fin_sum' ---
      // get current time
      t = fin_sumClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *text_5* updates
      if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        text_5.tStart = t;  // (not accounting for frame time here)
        text_5.frameNStart = frameN;  // exact frame index
        
        text_5.setAutoDraw(true);
      }
      
      
      // if text_5 is active this frame...
      if (text_5.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 1.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (text_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        text_5.tStop = t;  // not accounting for scr refresh
        text_5.frameNStop = frameN;  // exact frame index
        // update status
        text_5.status = PsychoJS.Status.FINISHED;
        text_5.setAutoDraw(false);
      }
      
      
      // *key_resp_2* updates
      if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        key_resp_2.tStart = t;  // (not accounting for frame time here)
        key_resp_2.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
      }
      frameRemains = 0.0 + 1.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (key_resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        key_resp_2.tStop = t;  // not accounting for scr refresh
        key_resp_2.frameNStop = frameN;  // exact frame index
        // update status
        key_resp_2.status = PsychoJS.Status.FINISHED;
        frameRemains = 0.0 + 1.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (key_resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          key_resp_2.tStop = t;  // not accounting for scr refresh
          key_resp_2.frameNStop = frameN;  // exact frame index
          // update status
          key_resp_2.status = PsychoJS.Status.FINISHED;
          key_resp_2.status = PsychoJS.Status.FINISHED;
            }
          
        }
        
        // if key_resp_2 is active this frame...
        if (key_resp_2.status === PsychoJS.Status.STARTED) {
          let theseKeys = key_resp_2.getKeys({keyList: [], waitRelease: false});
          _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
          if (_key_resp_2_allKeys.length > 0) {
            key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
            key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
            // a response ends the routine
            continueRoutine = false;
          }
        }
        
        // check for quit (typically the Esc key)
        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
        }
        
        // check if the Routine should terminate
        if (!continueRoutine) {  // a component has requested a forced-end of Routine
          routineForceEnded = true;
          return Scheduler.Event.NEXT;
        }
        
        continueRoutine = false;  // reverts to True if at least one component still running
        fin_sumComponents.forEach( function(thisComponent) {
          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
            continueRoutine = true;
          }
        });
        
        // refresh the screen if continuing
        if (continueRoutine && routineTimer.getTime() > 0) {
          return Scheduler.Event.FLIP_REPEAT;
        } else {
          return Scheduler.Event.NEXT;
        }
      };
    }
    
    
function fin_sumRoutineEnd(snapshot) {
      return async function () {
        //--- Ending Routine 'fin_sum' ---
        fin_sumComponents.forEach( function(thisComponent) {
          if (typeof thisComponent.setAutoDraw === 'function') {
            thisComponent.setAutoDraw(false);
          }
        });
        psychoJS.experiment.addData('fin_sum.stopped', globalClock.getTime());
        // update the trial handler
        if (currentLoop instanceof MultiStairHandler) {
          currentLoop.addResponse(key_resp_2.corr, level);
        }
        psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
        if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
            psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
            psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
            routineTimer.reset();
            }
        
        key_resp_2.stop();
        if (routineForceEnded) {
            routineTimer.reset();} else if (fin_sumMaxDurationReached) {
            fin_sumClock.add(fin_sumMaxDuration);
        } else {
            fin_sumClock.add(1.300000);
        }
        // Routines running outside a loop should always advance the datafile row
        if (currentLoop === psychoJS.experiment) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        return Scheduler.Event.NEXT;
      }
    }
    
    
var Get_pointsMaxDurationReached;
var _gp_key_resp_allKeys;
var Get_pointsMaxDuration;
var Get_pointsComponents;
function Get_pointsRoutineBegin(snapshot) {
      return async function () {
        TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
        
        //--- Prepare to start Routine 'Get_points' ---
        t = 0;
        frameN = -1;
        continueRoutine = true; // until we're told otherwise
        // keep track of whether this Routine was forcibly ended
        routineForceEnded = false;
        Get_pointsClock.reset();
        routineTimer.reset();
        Get_pointsMaxDurationReached = false;
        // update component parameters for each repeat
        textbox.setText('');
        textbox.refresh();
        gp_key_resp.keys = undefined;
        gp_key_resp.rt = undefined;
        _gp_key_resp_allKeys = [];
        psychoJS.experiment.addData('Get_points.started', globalClock.getTime());
        Get_pointsMaxDuration = null
        // keep track of which components have finished
        Get_pointsComponents = [];
        Get_pointsComponents.push(text_6);
        Get_pointsComponents.push(textbox);
        Get_pointsComponents.push(gp_key_resp);
        
        Get_pointsComponents.forEach( function(thisComponent) {
          if ('status' in thisComponent)
            thisComponent.status = PsychoJS.Status.NOT_STARTED;
           });
        return Scheduler.Event.NEXT;
      }
    }
    
    
function Get_pointsRoutineEachFrame() {
      return async function () {
        //--- Loop for each frame of Routine 'Get_points' ---
        // get current time
        t = Get_pointsClock.getTime();
        frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
        // update/draw components on each frame
        
        // *text_6* updates
        if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          text_6.tStart = t;  // (not accounting for frame time here)
          text_6.frameNStart = frameN;  // exact frame index
          
          text_6.setAutoDraw(true);
        }
        
        
        // if text_6 is active this frame...
        if (text_6.status === PsychoJS.Status.STARTED) {
        }
        
        
        // *textbox* updates
        if (t >= 0.0 && textbox.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          textbox.tStart = t;  // (not accounting for frame time here)
          textbox.frameNStart = frameN;  // exact frame index
          
          textbox.setAutoDraw(true);
        }
        
        
        // if textbox is active this frame...
        if (textbox.status === PsychoJS.Status.STARTED) {
        }
        
        
        // *gp_key_resp* updates
        if (t >= 3.0 && gp_key_resp.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          gp_key_resp.tStart = t;  // (not accounting for frame time here)
          gp_key_resp.frameNStart = frameN;  // exact frame index
          
          // keyboard checking is just starting
          psychoJS.window.callOnFlip(function() { gp_key_resp.clock.reset(); });  // t=0 on next screen flip
          psychoJS.window.callOnFlip(function() { gp_key_resp.start(); }); // start on screen flip
          psychoJS.window.callOnFlip(function() { gp_key_resp.clearEvents(); });
        }
        
        // if gp_key_resp is active this frame...
        if (gp_key_resp.status === PsychoJS.Status.STARTED) {
          let theseKeys = gp_key_resp.getKeys({keyList: 'space', waitRelease: false});
          _gp_key_resp_allKeys = _gp_key_resp_allKeys.concat(theseKeys);
          if (_gp_key_resp_allKeys.length > 0) {
            gp_key_resp.keys = _gp_key_resp_allKeys[_gp_key_resp_allKeys.length - 1].name;  // just the last key pressed
            gp_key_resp.rt = _gp_key_resp_allKeys[_gp_key_resp_allKeys.length - 1].rt;
            gp_key_resp.duration = _gp_key_resp_allKeys[_gp_key_resp_allKeys.length - 1].duration;
            // a response ends the routine
            continueRoutine = false;
          }
        }
        
        // check for quit (typically the Esc key)
        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
        }
        
        // check if the Routine should terminate
        if (!continueRoutine) {  // a component has requested a forced-end of Routine
          routineForceEnded = true;
          return Scheduler.Event.NEXT;
        }
        
        continueRoutine = false;  // reverts to True if at least one component still running
        Get_pointsComponents.forEach( function(thisComponent) {
          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
            continueRoutine = true;
          }
        });
        
        // refresh the screen if continuing
        if (continueRoutine) {
          return Scheduler.Event.FLIP_REPEAT;
        } else {
          return Scheduler.Event.NEXT;
        }
      };
    }
    
    
function Get_pointsRoutineEnd(snapshot) {
      return async function () {
        //--- Ending Routine 'Get_points' ---
        Get_pointsComponents.forEach( function(thisComponent) {
          if (typeof thisComponent.setAutoDraw === 'function') {
            thisComponent.setAutoDraw(false);
          }
        });
        psychoJS.experiment.addData('Get_points.stopped', globalClock.getTime());
        psychoJS.experiment.addData('textbox.text',textbox.text)
        gp_key_resp.stop();
        // the Routine "Get_points" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset();
        
        // Routines running outside a loop should always advance the datafile row
        if (currentLoop === psychoJS.experiment) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        return Scheduler.Event.NEXT;
      }
    }
    
    
var thanksMaxDurationReached;
var thanksMaxDuration;
var thanksComponents;
function thanksRoutineBegin(snapshot) {
      return async function () {
        TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
        
        //--- Prepare to start Routine 'thanks' ---
        t = 0;
        frameN = -1;
        continueRoutine = true; // until we're told otherwise
        // keep track of whether this Routine was forcibly ended
        routineForceEnded = false;
        thanksClock.reset(routineTimer.getTime());
        routineTimer.add(3.500000);
        thanksMaxDurationReached = false;
        // update component parameters for each repeat
        psychoJS.experiment.addData('thanks.started', globalClock.getTime());
        thanksMaxDuration = null
        // keep track of which components have finished
        thanksComponents = [];
        thanksComponents.push(text_th);
        
        thanksComponents.forEach( function(thisComponent) {
          if ('status' in thisComponent)
            thisComponent.status = PsychoJS.Status.NOT_STARTED;
           });
        return Scheduler.Event.NEXT;
      }
    }
    
    
function thanksRoutineEachFrame() {
      return async function () {
        //--- Loop for each frame of Routine 'thanks' ---
        // get current time
        t = thanksClock.getTime();
        frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
        // update/draw components on each frame
        
        // *text_th* updates
        if (t >= 0.0 && text_th.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          text_th.tStart = t;  // (not accounting for frame time here)
          text_th.frameNStart = frameN;  // exact frame index
          
          text_th.setAutoDraw(true);
        }
        
        
        // if text_th is active this frame...
        if (text_th.status === PsychoJS.Status.STARTED) {
        }
        
        frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (text_th.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          text_th.tStop = t;  // not accounting for scr refresh
          text_th.frameNStop = frameN;  // exact frame index
          // update status
          text_th.status = PsychoJS.Status.FINISHED;
          text_th.setAutoDraw(false);
        }
        
        // check for quit (typically the Esc key)
        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
        }
        
        // check if the Routine should terminate
        if (!continueRoutine) {  // a component has requested a forced-end of Routine
          routineForceEnded = true;
          return Scheduler.Event.NEXT;
        }
        
        continueRoutine = false;  // reverts to True if at least one component still running
        thanksComponents.forEach( function(thisComponent) {
          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
            continueRoutine = true;
          }
        });
        
        // refresh the screen if continuing
        if (continueRoutine && routineTimer.getTime() > 0) {
          return Scheduler.Event.FLIP_REPEAT;
        } else {
          return Scheduler.Event.NEXT;
        }
      };
    }
    
    
function thanksRoutineEnd(snapshot) {
      return async function () {
        //--- Ending Routine 'thanks' ---
        thanksComponents.forEach( function(thisComponent) {
          if (typeof thisComponent.setAutoDraw === 'function') {
            thisComponent.setAutoDraw(false);
          }
        });
        psychoJS.experiment.addData('thanks.stopped', globalClock.getTime());
        if (routineForceEnded) {
            routineTimer.reset();} else if (thanksMaxDurationReached) {
            thanksClock.add(thanksMaxDuration);
        } else {
            thanksClock.add(3.500000);
        }
        // Routines running outside a loop should always advance the datafile row
        if (currentLoop === psychoJS.experiment) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        return Scheduler.Event.NEXT;
      }
    }
    
    
var send_experiment_to_osfMaxDurationReached;
var send_experiment_to_osfMaxDuration;
var send_experiment_to_osfComponents;
function send_experiment_to_osfRoutineBegin(snapshot) {
      return async function () {
        TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
        
        //--- Prepare to start Routine 'send_experiment_to_osf' ---
        t = 0;
        frameN = -1;
        continueRoutine = true; // until we're told otherwise
        // keep track of whether this Routine was forcibly ended
        routineForceEnded = false;
        send_experiment_to_osfClock.reset(routineTimer.getTime());
        routineTimer.add(2.000000);
        send_experiment_to_osfMaxDurationReached = false;
        // update component parameters for each repeat
        psychoJS.experiment.addData('send_experiment_to_osf.started', globalClock.getTime());
        send_experiment_to_osfMaxDuration = null
        // keep track of which components have finished
        send_experiment_to_osfComponents = [];
        send_experiment_to_osfComponents.push(text_7);
        
        send_experiment_to_osfComponents.forEach( function(thisComponent) {
          if ('status' in thisComponent)
            thisComponent.status = PsychoJS.Status.NOT_STARTED;
           });
        return Scheduler.Event.NEXT;
      }
    }
    
    
function send_experiment_to_osfRoutineEachFrame() {
      return async function () {
        //--- Loop for each frame of Routine 'send_experiment_to_osf' ---
        // get current time
        t = send_experiment_to_osfClock.getTime();
        frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
        // update/draw components on each frame
        
        // *text_7* updates
        if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          text_7.tStart = t;  // (not accounting for frame time here)
          text_7.frameNStart = frameN;  // exact frame index
          
          text_7.setAutoDraw(true);
        }
        
        
        // if text_7 is active this frame...
        if (text_7.status === PsychoJS.Status.STARTED) {
        }
        
        frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (text_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          text_7.tStop = t;  // not accounting for scr refresh
          text_7.frameNStop = frameN;  // exact frame index
          // update status
          text_7.status = PsychoJS.Status.FINISHED;
          text_7.setAutoDraw(false);
        }
        
        // check for quit (typically the Esc key)
        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
        }
        
        // check if the Routine should terminate
        if (!continueRoutine) {  // a component has requested a forced-end of Routine
          routineForceEnded = true;
          return Scheduler.Event.NEXT;
        }
        
        continueRoutine = false;  // reverts to True if at least one component still running
        send_experiment_to_osfComponents.forEach( function(thisComponent) {
          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
            continueRoutine = true;
          }
        });
        
        // refresh the screen if continuing
        if (continueRoutine && routineTimer.getTime() > 0) {
          return Scheduler.Event.FLIP_REPEAT;
        } else {
          return Scheduler.Event.NEXT;
        }
      };
    }
    
    
function send_experiment_to_osfRoutineEnd(snapshot) {
      return async function () {
        //--- Ending Routine 'send_experiment_to_osf' ---
        send_experiment_to_osfComponents.forEach( function(thisComponent) {
          if (typeof thisComponent.setAutoDraw === 'function') {
            thisComponent.setAutoDraw(false);
          }
        });
        psychoJS.experiment.addData('send_experiment_to_osf.stopped', globalClock.getTime());
        if (routineForceEnded) {
            routineTimer.reset();} else if (send_experiment_to_osfMaxDurationReached) {
            send_experiment_to_osfClock.add(send_experiment_to_osfMaxDuration);
        } else {
            send_experiment_to_osfClock.add(2.000000);
        }
        // Routines running outside a loop should always advance the datafile row
        if (currentLoop === psychoJS.experiment) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        return Scheduler.Event.NEXT;
      }
    }
    
    
function importConditions(currentLoop) {
      return async function () {
        psychoJS.importAttributes(currentLoop.getCurrentTrial());
        return Scheduler.Event.NEXT;
        };
    }
    
    
async function quitPsychoJS(message, isCompleted) {
      // Check for and save orphaned data
      if (psychoJS.experiment.isEntryEmpty()) {
        psychoJS.experiment.nextEntry();
      }
      // 1. Disable default browser download
      psychoJS._saveResults = 0;
      
      // 2. Generate filename
      let filename = psychoJS._experiment._experimentName + '_' + psychoJS._experiment._datetime + '.csv';
      
      // 3. Extract data
      let dataObj = psychoJS._experiment._trialsData;
      
      console.group('DataPipe Debugging');
      console.log('Total rows in dataObj:', dataObj.length);
      console.log('Sample of first row:', dataObj[0]);
      console.log('Sample of last row:', dataObj[dataObj.length - 1]);
      
      // --- ROBUST CSV CONSTRUCTION ---
      const SEP = ';'; 
      
      // A. Collect EVERY unique key present in the entire experiment
      let headers = [];
      dataObj.forEach((trial, index) => {
          if (typeof trial !== 'object' || trial === null) {
              console.warn(`Row ${index} is not a valid object:`, trial);
              return;
          }
          Object.keys(trial).forEach(key => {
              if (!headers.includes(key)) {
                  headers.push(key);
              }
          });
      });
      
      console.log('Total unique columns identified:', headers.length);
      console.log('Columns list:', headers);
      
      // B. Helper to escape/quote values
      const formatCell = (val) => {
          if (val === null || val === undefined) return '';
          let str = (typeof val === 'object') ? JSON.stringify(val) : String(val);
          if (str.includes(SEP) || str.includes('"') || str.includes('\n') || str.includes('\r')) {
              str = '"' + str.replace(/"/g, '""') + '"';
          }
          return str;
      };
      
      // C. Build CSV string
      let csvRows = [];
      csvRows.push(headers.join(SEP));
      
      dataObj.forEach((rowObj, index) => {
          // Ensure we handle rows that might not be objects
          if (typeof rowObj !== 'object' || rowObj === null) {
              csvRows.push(new Array(headers.length).fill('').join(SEP));
              return;
          }
          const rowValues = headers.map(h => formatCell(rowObj[h]));
          csvRows.push(rowValues.join(SEP));
      });
      
      let data = csvRows.join('\n');
      console.log('Final CSV string length:', data.length);
      console.groupEnd();
      
      // 4. Send to OSF via DataPipe
      console.log('Sending to DataPipe...');
      fetch('https://pipe.jspsych.org/api/data', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              Accept: '*/*',
          },
          body: JSON.stringify({
              experimentID: 'H1r1lSmRRNeY', 
              filename: filename,
              data: data,
          }),
      }).then(response => {
          console.log('DataPipe Response Status:', response.status);
          return response.json();
      }).then(data => {
          console.log('DataPipe Server Response:', data);
          // quitPsychoJS(); // Commented out for debugging so you can read the console
      }).catch(err => {
          console.error('Save failed:', err);
          // quitPsychoJS();
      });
      psychoJS.window.close();
      psychoJS.quit({message: message, isCompleted: isCompleted});
      
      return Scheduler.Event.QUIT;
    }
