from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="ClumpLabel/text",
    text='DRY')
    .es(1)
    .pt(1)
    .fr(1)
    .ja('原音')
    .ko('원음')
    .zhHans('干声')
    .zhHant('乾聲')
    .ar('جاف')
    .he('מיקס')
)

ts.append(T(tag="ClumpLabel/text",
    text='FILTER')
    .es('FILTRO')
    .pt('FILTRO')
    .fr('FILTRE')
    .ja('フィルター')
    .ko('필터')
    .zhHans('滤波')
    .zhHant('濾波')
    .ar('الفِلتر')
    .he('פילטר')
)

ts.append(T(tag="ClumpLabel/text",
    text='GAIN+')
    .es('GANANCIA+')
    .pt('GANHO+')
    .fr(1)
    .ja('ゲイン＋')
    .ko('게인+')
    .zhHans('增益+')
    .zhHant('增益+')
    .ar('+ربح')
    .he('גיין ועוד')
)

ts.append(T(tag="ClumpLabel/text",
    text='GATE')
    .es('PUERTA')
    .pt(1)
    .fr(1)
    .ja('ゲート')
    .ko('게이트')
    .zhHans('门限')
    .zhHant('門限')
    .ar('بوابة')
    .he('גייט')
)

ts.append(T(tag="ClumpLabel/text",
    text='GATE+')
    .es('PUERTA+')
    .pt(1)
    .fr(1)
    .ja('ゲート＋')
    .ko('게이트+')
    .zhHans('门限+')
    .zhHant('門限+')
    .ar('+بوابة')
    .he('גייט ועוד')
)

ts.append(T(tag="ClumpLabel/text",
    text='LOFI')
    .es(1)
    .pt(1)
    .fr(1)
    .ja('ローファイ')
    .ko('로우파이')
    .zhHans('低保真度')
    .zhHant('低傳真度')
    .ar(1)
    .he('לו-פיי')
)

ts.append(T(tag="ClumpLabel/text",
    text='REVERB')
    .es(1)
    .pt('REVERBERAÇÃO')
    .fr(1)
    .ja('リバーブ')
    .ko('리버브')
    .zhHans('混响')
    .zhHant('混響')
    .ar('الصدى')
    .he('ריוורב')
)

ts.append(T(tag="ClumpLabel/text",
    text='STEREO')
    .es('ESTÉREO')
    .pt('ESTÉREO')
    .fr('STÉRÉO')
    .ja('ステレオ')
    .ko('스테레오')
    .zhHans('立体声')
    .zhHant('立體聲')
    .ar('إستريو')
    .he('סטריאו')
)

ts.append(T(tag="ParamLabel/text",
    text='Analog')
    .es('Análogo')
    .pt('Analógico')
    .fr('Analogique')
    .ja('アナログ')
    .ko('아날로그')
    .zhHans('模拟')
    .zhHant('類比')
    .ar('أنالوج')
    .he('אנלוג')
)

ts.append(T(tag="ParamLabel/text",
    text='Attack')
    .es('Ataque')
    .pt('Ataque')
    .fr('Attaque')
    .ja('アタック')
    .ko('어택')
    .zhHans('起动')
    .zhHant('起動')
    .ar('زمن التطبيق')
    .he('זמן התקף')
)

ts.append(T(tag="ParamLabel/text",
    text='Bass Width')
    .es('Ancho de Graves')
    .pt('Abertura: Graves')
    .fr('Largeur des Graves')
    .ja('低域幅')
    .ko('저역 폭')
    .zhHans('低频宽度')
    .zhHant('低頻寬度')
    .ar('وسع الباس')
    .he('רוחב בס')
)

ts.append(T(tag="ParamLabel/text",
    text='Bias')
    .es(1)
    .pt('Inclinação')
    .fr('Tension')
    .ja('バイアス')
    .ko('바이어스')
    .zhHans('交流偏磁')
    .zhHant('交流偏磁')
    .ar('الانحياز')
    .he('ביאס')
)

ts.append(T(tag="ParamLabel/text",
    text='Crosstalk')
    .es('Diafonía')
    .pt('Diafonia')
    .fr('Diaphonie')
    .ja('クロストーク')
    .ko('크로스토크')
    .zhHans('声道串扰')
    .zhHant('聲道串擾')
    .ar('تَشْوِيشٌ تَدَاخُلِيٌّ')
    .he('קרוס-טוק')
)

ts.append(T(tag="ParamLabel/text",
    text='Damping')
    .es('Amortiguación')
    .pt('Absorção')
    .fr('Absorption')
    .ja('ダンピング')
    .ko('댐핑')
    .zhHans('阻尼')
    .zhHant('阻尼')
    .ar('التخميد')
    .he('דעיכה')
)

ts.append(T(tag="ParamLabel/text",
    text='Decay')
    .es('Decaimiento')
    .pt('Decaimento')
    .fr(1)
    .ja('ディケイ')
    .ko('디케이')
    .zhHans('衰减')
    .zhHant('衰減')
    .ar('التَّضَاؤُلِ')
    .he('דיקאיי')
)

ts.append(T(tag="ParamLabel/text",
    text='Detection')
    .es('Detección')
    .pt('Detecção')
    .fr('Détection')
    .ja('ディテクション')
    .ko('디텍션')
    .zhHans('侦测')
    .zhHant('偵測')
    .ar('الكشف')
    .he('דיטקשין')
)

ts.append(T(tag="ParamLabel/text",
    text='Digital')
    .es(1)
    .pt(1)
    .fr('Numérique')
    .ja('デジタル')
    .ko('디지털')
    .zhHans('数位')
    .zhHant('數位')
    .ar('رقمي')
    .he('דיגיטל')
)

ts.append(T(tag="ParamLabel/text",
    text='Dry Gain')
    .es('Ganancia Dry')
    .pt('Ganho: Dry')
    .fr('Gain Dry')
    .ja('ドライゲイン')
    .ko('원음 게인')
    .zhHans('干声增益')
    .zhHant('乾聲增益')
    .ar('الجاف')
    .he('גיין')
)

ts.append(T(tag="ParamLabel/text",
    text='Mode')
    .es('Modo')
    .pt('Modo')
    .fr(1)
    .ja('モード')
    .ko('모드')
    .zhHans('模式')
    .zhHant('模式')
    .ar('الوضع')
    .he('מצב')
)

ts.append(T(tag="ParamLabel/text",
    text='Predelay')
    .es('Pre-retraso')
    .pt('Pré-delay')
    .fr('Pré-delay')
    .ja('プリディレイ')
    .ko('프리딜레이')
    .zhHans('预先延迟')
    .zhHant('預先延遲')
    .ar('ما قبل التأخير الزمني')
    .he('פרה-דיליי')
)

ts.append(T(tag="ParamLabel/text",
    text='Range')
    .es('Rango')
    .pt('Extensão')
    .fr('Gamme')
    .ja('範囲')
    .ko('필터 범위')
    .zhHans('范围')
    .zhHant('範圍')
    .ar('المدَى')
    .he('טווח')
)

ts.append(T(tag="ParamLabel/text",
    text='Release')
    .es('Relajación')
    .pt('Repouso')
    .fr('Retour')
    .ja('リリース')
    .ko('릴리즈')
    .zhHans('释放')
    .zhHant('釋放')
    .ar('التحرير')
    .he('זמן שחרור')
)

ts.append(T(tag="ParamLabel/text",
    text='Sensitivity')
    .es('Sensibilidad')
    .pt('Sensibilidade')
    .fr('Sensibilité')
    .ja('センシティビティー')
    .ko('감도')
    .zhHans('感度')
    .zhHant('感度')
    .ar('الحساسية')
    .he('רגישות')
)

ts.append(T(tag="ParamLabel/text",
    text='Sidechain Source')
    .es('Fuente de Sidechain')
    .pt('Fonte do Sidechain')
    .fr('Source de Sidechain')
    .ja('サイドチェインソース')
    .ko('사이드체인 소스')
    .zhHans('旁链声源')
    .zhHant('旁鏈聲源')
    .ar('منبع السايدشين')
    .he('מקור סייד-צ׳יין')
)

ts.append(T(tag="ParamLabel/text",
    text='Target')
    .es('Objetivo')
    .pt('Alvo')
    .fr('Cible')
    .ja('ターゲット')
    .ko('타겟')
    .zhHans('目标')
    .zhHant('目標')
    .ar('الهدف')
    .he('מטרה')
)

ts.append(T(tag="ParamLabel/text",
    text='Treble Width')
    .es('Ancho de Altos')
    .pt('Abertura: Agudos')
    .fr('Largeur des Aigus')
    .ja('高域幅')
    .ko('고역 폭')
    .zhHans('高频宽度')
    .zhHant('高頻寬度')
    .ar('وسع الصوت العالي')
    .he('רוחב טרבל')
)

ts.append(T(tag="ParamLabel/text",
    text='Wet Gain')
    .es('Ganancia Wet')
    .pt('Ganho: Wet')
    .fr('Gain Wet')
    .ja('ウェットゲイン')
    .ko('리버브 게인')
    .zhHans('混响增益')
    .zhHant('混響增益')
    .ar('الربح الرطب')
    .he('גיין אפקט')
)

ts.append(T(tag="Parameter/option",
    context="GateDetection",
    text='Classic')
    .es('Clásica')
    .pt('Clássico')
    .fr('Classique')
    .ja('クラシック')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('تقليدي')
    .he('קלאסי')
)

ts.append(T(tag="Parameter/option",
    context="GateDetection",
    text='Dynamic')
    .es('Dinámica')
    .pt('Dinâmico')
    .fr('Dynamique')
    .ja('ダイナミック')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('ديناميكي')
    .he('דינאמי')
)

ts.append(T(tag="Parameter/option",
    context="GateDetection",
    text='Transient')
    .es('Transitoria')
    .pt('Transientes')
    .fr('Transitoire')
    .ja('トランジェント')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('الترَانْزيْنت')
    .he('טרנזיאנט')
)

ts.append(T(tag="Parameter/option",
    context="GateMode",
    text='Duck')
    .es('Ducking')
    .pt(1)
    .fr(1)
    .ja('ダック')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('التَّمَلص')
    .he('דאקינג')
)

ts.append(T(tag="Parameter/option",
    context="GateMode",
    text='Gate')
    .es('Puerta')
    .pt(1)
    .fr(1)
    .ja('ゲート')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('البوابة')
    .he('גייט')
)

ts.append(T(tag="Parameter/option",
    context="GateTarget",
    text='Dry')
    .es(1)
    .pt(1)
    .fr(1)
    .ja('ドライ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('جاف')
    .he('יבש')
)

ts.append(T(tag="Parameter/option",
    context="GateTarget",
    text='Dry + Wet')
    .es(1)
    .pt(1)
    .fr(1)
    .ja('ドライ＋ウェット')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('جاف + رطب')
    .he('יבש+רטוב')
)

ts.append(T(tag="Parameter/option",
    context="GateTarget",
    text='Dry + Wet Pre')
    .es(1)
    .pt('Dry + Wet Pré')
    .fr('Dry + Wet Pré')
    .ja('ドライ＋ウェットプリ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('(جاف + رطب (ما قبل')
    .he('יבש+רטוב פרה פיידר')
)

ts.append(T(tag="Parameter/option",
    context="GateTarget",
    text='Wet')
    .es(1)
    .pt(1)
    .fr(1)
    .ja('ウェット')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('رطب')
    .he('רטוב')
)

ts.append(T(tag="Parameter/option",
    context="GateTarget",
    text='Wet Pre')
    .es(1)
    .pt('Wet Pré')
    .fr('Wet Pré')
    .ja('ウェットプリ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('(رطب (ما قبل')
    .he('רטוב פרה פיידר')
)

ts.append(T(tag="Tagline",
    text='Incredibly good bad reverb')
    .es('Mala reverberación, mejor que nunca.')
    .pt('Reverberação ruim, com excelência.')
    .fr('Mauvaise reverb incroyablement bonne.')
    .ja('ヤバすぎるリバーブ')
    .ko('美친 리버브')
    .zhHans('混响史上的最好与最坏')
    .zhHant('混響史上的最好與最壞')
    .ar('صدى جيد وسيء، بشكلٍ لا يصدق')
    .he('.ריוורב שהוא גם מדהים וגם גרוע שזה לא ייאמן')
)

