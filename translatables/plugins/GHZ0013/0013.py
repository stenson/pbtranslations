from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="ClumpLabel/text",
    text='MID')
    .es(1)
    .pt('MEIO')
    .fr(1)
    .ja('ミッド')
    .ko('미드')
    .zhHans('中')
    .zhHant('中')
    .ar('ميد')
    .he('אמצע')
)

ts.append(T(tag="ClumpLabel/text",
    text='MID PAN')
    .es('PANO MID')
    .pt(1)
    .fr('PAN MID')
    .ja('ミッドパン')
    .ko('미드 패닝')
    .zhHans('中声像')
    .zhHant('中聲像')
    .ar('تدوير ميد')
    .he('פאנינג אמצע')
)

ts.append(T(tag="ClumpLabel/text",
    text='MID TILT')
    .es('INCLINACIÓN MID')
    .pt('INCLINAÇÃO–MEIO')
    .fr('INCLINAISON MID')
    .ja('ミッドチルト')
    .ko('미드 틸트')
    .zhHans('中信号倾斜')
    .zhHant('中信號傾斜')
    .ar('إمالة الميد')
    .he('טילט אמצע')
)

ts.append(T(tag="ClumpLabel/text",
    text='MONO BELOW')
    .es('CENTRALIZADOR DE BAJOS')
    .pt('CENTRALIZAR GRAVES')
    .fr('FILTRE MONO BAS')
    .ja('低域モノラルフィルター')
    .ko('저역 모노화')
    .zhHans('低频单声道化')
    .zhHant('低頻單聲道化')
    .ar('خرج أحادي تحت')
    .he('מונו')
)

ts.append(T(tag="ClumpLabel/text",
    text='SIDE')
    .es(1)
    .pt('LADOS')
    .fr(1)
    .ja('サイド')
    .ko('사이드')
    .zhHans('侧')
    .zhHant('側')
    .ar('سايد')
    .he('צדדים')
)

ts.append(T(tag="ClumpLabel/text",
    text='SIDE PAN')
    .es('PANO SIDE')
    .pt(1)
    .fr('PAN SIDE')
    .ja('サイドパン')
    .ko('사이드 패닝')
    .zhHans('侧声像')
    .zhHant('側聲像')
    .ar('تدوير سايد')
    .he('פאנינג צדדים')
)

ts.append(T(tag="ClumpLabel/text",
    text='SIDE TILT')
    .es('INCLINACIÓN SIDE')
    .pt('INCLINAÇÃO–LADOS')
    .fr('INCLINAISON SIDE')
    .ja('サイドチルト')
    .ko('사이드 틸트')
    .zhHans('侧信号倾斜')
    .zhHant('側信號傾斜')
    .ar('إمالة السايد')
    .he('טילט צדדים')
)

ts.append(T(tag="ParamLabel/text",
    text='Bass Makeup')
    .es('Compensación de Graves')
    .pt('Compensar Grave')
    .fr('Gain des Graves')
    .ja('低域ゲイン補償')
    .ko('저역 게인 보상')
    .zhHans('低频增益补充')
    .zhHant('低頻增益補充')
    .ar('تعويض الباس')
    .he('פיצוי בס')
)

ts.append(T(tag="ParamLabel/text",
    text='Flip L/R')
    .es('Invertir L/R')
    .pt('Inverter L/R')
    .fr('Inverser L/R')
    .ja('L/R入れ替え')
    .ko('좌/우 뒤집기')
    .zhHans('L/R翻转')
    .zhHant('L/R翻轉')
    .ar('L/R عَكّس')
    .he('היפוך ימין/שמאל')
)

ts.append(T(tag="ParamLabel/text",
    text='Frequency')
    .es('Frecuencia')
    .pt('Frequência')
    .fr('Fréquence')
    .ja('基準周波数')
    .ko('기준 프리퀀시')
    .zhHans('频率')
    .zhHant('頻率')
    .ar('التردد')
    .he('תדר')
)

ts.append(T(tag="ParamLabel/text",
    text='Input Mode')
    .es('Modo de Entrada')
    .pt('Modo de Entrada')
    .fr("Mode d'Entrée")
    .ja('インプットモード')
    .ko('인풋 모드')
    .zhHans('输入模式')
    .zhHant('輸入模式')
    .ar('وضع إشارة الإدخال')
    .he('מצב כניסה')
)

ts.append(T(tag="ParamLabel/text",
    text="""
        Loudness
        Mode""")
    .es("""
        Modo de
        Volumen""")
    .pt("""
        Modo de
        Intensidade""")
    .fr("""
        Mode
        de Sonie""")
    .ja('ラウドネスモード')
    .ko('음량 모드')
    .zhHans('响度模式')
    .zhHant('響度模式')
    .ar("""
        مستوَى الصوت
        وضع""")
    .he('לאודנס')
)

ts.append(T(tag="ParamLabel/text",
    text='Output Mode')
    .es('Modo de Salida')
    .pt('Modo de Saída')
    .fr('Mode de Sortie')
    .ja('アウトプットモード')
    .ko('아웃풋 모드')
    .zhHans('输出模式')
    .zhHant('輸出模式')
    .ar('وضع إشارة الإخراج')
    .he('מצב יציאה')
)

ts.append(T(tag="ParamLabel/text",
    text='Range')
    .es('Rango')
    .pt('Extensão')
    .fr('Gamme')
    .ja('範囲')
    .ko('범위')
    .zhHans('范围')
    .zhHant('範圍')
    .ar('المدَى')
    .he('טווח')
)

ts.append(T(tag="ParamLabel/text",
    text='Stereo Width')
    .es('Amplitud Estéreo')
    .pt('Abertura do Estéreo')
    .fr('Largeur Stéréo')
    .ja('ステレオ幅')
    .ko('스테레오 폭')
    .zhHans('立体声宽度')
    .zhHant('立體聲寬度')
    .ar('وُسع الإشَارة إستِيريُو')
    .he('רוחב סטריאו')
)

ts.append(T(tag="ParamLabel/text",
    text='Strength')
    .es('Magnitud')
    .pt('Força')
    .fr('Force')
    .ja('調節')
    .ko('필터 조절')
    .zhHans('强度')
    .zhHant('強度')
    .ar('الشدة')
    .he('עוצמה')
)

ts.append(T(tag="ParamLabel/text",
    text='Width Mode')
    .es('Modo de Amplitud')
    .pt('Modo de Abertura')
    .fr('Mode de Largeur')
    .ja('幅モード')
    .ko('스테레오 폭 모드')
    .zhHans('宽度模式')
    .zhHant('寬度模式')
    .ar('وضع الوُسع')
    .he('מצב רוחב')
)

ts.append(T(tag="Parameter/option",
    text='MUTE')
    .es('1')
    .pt('MUDO')
    .fr(1)
    .ja('ミゥート')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('كتم الصوت')
    .he('השתק')
)

ts.append(T(tag="Parameter/option",
    text='SOLO')
    .es(1)
    .pt(1)
    .fr(1)
    .ja('ソロ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('صولو')
    .he('סולו')
)

ts.append(T(tag="Parameter/option",
    context="FlipLR",
    text='Left | Right')
    .es('Izquierda | Derecha')
    .pt('L | R')
    .fr('Gauche | Droite')
    .ja('左｜右')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('L | R')
    .he('ימין|שמאל')
)

ts.append(T(tag="Parameter/option",
    context="FlipLR",
    text='Right | Left')
    .es('Derecha | Izquierda')
    .pt('R | L')
    .fr('Droite | Gauche')
    .ja('右｜左')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('R | L')
    .he('שמאל|ימין')
)

ts.append(T(tag="Parameter/option",
    context="InputMode",
    text='Left | Right')
    .es('Izquierda | Derecha')
    .pt('L | R')
    .fr('Gauche | Droite')
    .ja('左｜右')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('L | R')
    .he('ימין|שמאל')
)

ts.append(T(tag="Parameter/option",
    context="InputMode",
    text='Mid | Side')
    .es(1)
    .pt('Meio | Lados')
    .fr(1)
    .ja('ミッド｜サイド')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('ميد-سايد')
    .he('אמצע|צדדים')
)

ts.append(T(tag="Parameter/option",
    context="MidTiltLoudnessMode",
    text='Auto')
    .es('Automático')
    .pt('Automático')
    .fr('Automatique')
    .ja('自動')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('تلقائي')
    .he('אוטומטי')
)

ts.append(T(tag="Parameter/option",
    context="MidTiltLoudnessMode",
    text='Bass')
    .es('Graves')
    .pt('Graves')
    .fr('Grave')
    .ja('低域')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('الباس')
    .he('בס')
)

ts.append(T(tag="Parameter/option",
    context="MidTiltLoudnessMode",
    text='Standard')
    .es('Estándar')
    .pt('Padrão')
    .fr('Normal')
    .ja('普通')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('عادي')
    .he('סטנדרט')
)

ts.append(T(tag="Parameter/option",
    context="MidTiltLoudnessMode",
    text='Treble')
    .es('Agudos')
    .pt('Agudos')
    .fr('Aigu')
    .ja('高域')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('الصوت العالي')
    .he('טרבל')
)

ts.append(T(tag="Parameter/option",
    context="StereoWidthMode",
    text='M/S Blend')
    .es('Mezcla M/S')
    .pt('Mescla Meio/Lados')
    .fr('Mélange M/S')
    .ja('M/Sブレンド')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('M/S مزج ال')
    .he('מיקס אמצע/צדדים')
)

ts.append(T(tag="Parameter/option",
    context="StereoWidthMode",
    text='Natural')
    .es(1)
    .pt(1)
    .fr('Naturel')
    .ja('ナチュラル')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('طبيعي')
    .he('טבעי')
)

ts.append(T(tag="Parameter/option",
    context="StereoWidthMode",
    text='Shuffler A')
    .es('Modo Aleatorio A')
    .pt('Embaralhar A')
    .fr('Brouilleur A')
    .ja('シャッフルA')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('A الملخبط')
    .he('שאפל א׳')
)

ts.append(T(tag="Parameter/option",
    context="StereoWidthMode",
    text='Shuffler B')
    .es('Modo Aleatorio B')
    .pt('Embaralhar B')
    .fr('Brouilleur B')
    .ja('シャッフルB')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('B الملخبط')
    .he('שאפל ב׳')
)

ts.append(T(tag="Parameter/option",
    context="StereoWidthMode",
    text='Shuffler C')
    .es('Modo Aleatorio C')
    .pt('Embaralhar C')
    .fr('Brouilleur C')
    .ja('シャッフルC')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('C الملخبط')
    .he('שאפל ג׳')
)

ts.append(T(tag="Parameter/option",
    context="StereoWidthMode",
    text='Standard')
    .es('Estándar')
    .pt('Padrão')
    .fr('Normal')
    .ja('普通')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('عادي')
    .he('סטנדרט')
)

ts.append(T(tag="Tagline",
    text='Expressive stereo imaging.')
    .es('Imagen estéreo expresiva.')
    .pt('Expressividade na imagem estéreo.')
    .fr('Image stéréo expressive.')
    .ja('ステレオイメージャーの集結と結合')
    .ko('최고의 스테레오 이미징')
    .zhHans('生动的立体声')
    .zhHant('生動的立體聲')
    .ar('تصوير إستيريو مُعَبِّر')
    .he('סטריאו אימג׳ינג אקספרסיבי')
)

