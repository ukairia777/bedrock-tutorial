# Langchain 패키지들
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import BedrockChat
import boto3
import json

session = boto3.Session()

bedrock = session.client(
    service_name='bedrock-runtime',
    region_name='us-east-1',
    endpoint_url="https://bedrock-runtime.us-east-1.amazonaws.com"
)

# https://n.news.naver.com/mnews/article/020/0003538408?sid=100

script = '''허수현은 한반도 최북단 탄광마을이 낳은 수재였다. 그는 고등학교 졸업 직전 북한 전체에서 700명에게만 수여하는 ‘7.15 최우등상’을 수상했다. 7.15최우등상은 김정일이 평양 남산고급중학교를 졸업한 날인 1960년 7월 15일을 기념해 1987년에 만들어진 상이다.

지금은 이 상이 특권층 자식들을 대학에 보내기 위한 발판이 돼 각종 비리와 뇌물로 얼룩져 있지만, 상이 제정된 초기 몇 년은 정말 공부 잘하는 사람에게만 수여됐다. 상을 받게 되면 곧바로 중앙급 대학에 진학할 수 있었다. 북한에선 고등중학교 졸업생 중 20% 미만이 대학이나 전문학교에 갈 수 있다는 것을 감안하면 엄청난 특혜였다.

허 씨도 김책공업종합대학(김책공대)에 입학해 8년이나 공부했다. 그리고 그때 배운 지식을 활용해 지금은 한반도 최남단인 경남 마산의 해저터널 공사장에서 시공품질을 관리하는 공사차장으로 일하고 있다. 김책공대 졸업생이 네 번의 탈북을 반복한 뒤 건강이 악화돼 남의 등에 업혀 동남아 정글을 넘어 한국까지 오게 되고, 이후 남과 북에서 동시에 측량기사 자격을 받은 최초의 기술자가 돼 해저터널 공사장에서 일하게 되기까지 삶의 과정은 결코 순탄하지 않았다.


2021년 강원도 동해시 한 아파트 공사장에서 시공 측량 작업을 진행하고 있는 허 씨.


● 신분 상승의 꿈
그가 태어난 한반도 최북단 온성군은 오랜 역사를 가지고 있다. 세종 22년인 1440년에 김종서 장군이 이곳을 평정한 뒤 군을 설치하고 온성이라 부르기 시작했다.

온성에는 평안남도 안주 탄전에 이은 북한 최대의 갈탄 탄전이 있다. 1980년대까지만 해도 온성에는 연간 50만 톤 이상의 갈탄을 생산하는 탄광이 여러 개 있었다. 허 씨는 이런 대형 탄광 중 하나인 주원 탄광마을에서 1974년에 태어났다.

탄광에서 일하는 사람들은 대개 출신성분이 나빴다. 허 씨의 부친도 마찬가지였다. 부친은 1960년대 후반까지 중국에서 살다가 문화대혁명 등의 격변기를 거치며 북한으로 넘어왔다.
부친은 늘 허 씨에게 “너는 공부를 잘해 꼭 신분 상승을 해야 한다”고 말했다. 허 씨가 13세 때 부친은 갱이 붕괴돼 사망했다. 탄광마을에선 자주 일어나는 일이었다.

아버지가 사망하자 허 씨는 1년 정도 방황했다. 학교에도 나가지 않았다. 하지만 곧 마음을 다잡고, 부친의 소원대로 신분 상승을 하기로 결심했다. 3년을 열심히 공부해 고등학교 졸업반이 됐을 때 허 씨는 7.15 최우등상을 받을 정도로 공부를 잘하게 됐다. 북한도 대도시의 교육 환경이 매우 좋기 때문에 외진 탄광마을에서 수상자를 배출한다는 것은 하늘의 별 따기였다.

하지만 상을 받아도 문제였다. 평양에서 대학을 다닌다는 것은 가족들에겐 엄청난 희생이 필요한 일이었다. 그런데 그가 김책공대에 입학한 1992년엔 탄광마을에 배급이 제대로 공급되지 않았다. 평양에서 대학을 다닐 돈이 나올 리 만무했다.

허 씨는 대학 대신에 군대에 가려고 시도했다. 대학을 갈 사정이 못되니 군에 입대해 노동당원이 되면 신분이 그나마 좀 바뀔 것이라고 생각했던 것이다.

하지만 7.15 최우등상 수상자는 군대에 보내지 않는다는 지침이 있어 결국 갈 수는 없었다. 그는 울며 겨자 먹기로 김책공대 지질탐사학부에 입학했다.

그해 온성에서 중앙대학에 입학한 사람은 단 두 명이었다. 허 씨 외에 이과대학 입학생이 한 명 더 있었다. 온성군은 그런 동네였다.

● 돈에 성적을 뺏기던 시절
북한의 다양한 산업현장에서 활약하는 인재들을 키우는 김책공대는 학제가 길어 7년을 다녀야 졸업증을 받을 수 있다. 그런데 대학을 다니며 각종 공사현장에 끌려 다니다 보니 진도가 밀려 7년 안에 졸업하기가 어렵다. 허 씨도 학제보다 1년을 더 다녀 2000년에야 졸업할 수 있었다.

그가 대학을 다니던 1990년대 중반은 북한에서 고난의 행군 시기라 사방에서 아사자가 속출할 때였다. 대학 기숙사에서 주는 밥을 먹으면 굶어죽을 수밖에 없었다.

탄광마을에서 태어나 김책공대에 입학한 허 씨와, 어촌마을에서 태어나 김일성대에 입학한 기자는 평양에서 대학을 다닌 시기가 정확히 겹친다. 그래서 인터뷰 내내 떠올리기 싫은 추억들이 소환됐다. 몇 개를 소개하면 이런 식이다.

“1993년 공화국 창건 행사 때 김일성대 학생들은 깃발을 들고 김일성광장을 통과했습니다. 그 연습만 3개월 하면서 너무 힘들어 죽을 뻔 했죠.”

“김책공대는 촛불을 들고 김일성대를 따라갔죠. 저도 죽을 뻔 했어요.”

“제대군인인 학급 소대장, 청년단체비서 이런 사람들은 가난한데 공부 잘하는 학생들을 곁에 한둘씩 끼고 있죠. 그리곤 시험 때마다 자기 것도 좀 써달라고 사정하죠. 그걸 거절하기 어려워 저는 시험 칠 때마다 시험지 3개를 써주었어요. 다양한 볼펜을 준비해서 한 장은 정자로 쓰고, 다른 장은 흘겨 쓰고, 이런 식으로 답을 적어 교수가 뒤돌아서 있을 때 공부 못하는 제대군인들에게 몰래 건네주었죠. 대신 그들은 각종 비용을 걷을 때 나를 빼주기도 했고, 가끔 도시락도 두 개를 갖고 와서 허기진 배도 채워주었습니다.”

“저도 그랬어요. 국가졸업시험 때까지 남의 시험지를 작성해주었어요. 대신 저는 돈을 받았습니다. 방학 때 집에 가지도 않았지요. 온성까지 기차로 일주일 넘게 걸리는데 왔다갔다 시간 낭비가 크고, 또 가봐야 집에서 보태줄 수도 없으니 방학 때는 제대군인들 과외를 해주고 돈을 받았습니다.”

“저는 졸업장을 받고 나니, 3점짜리 과목이 몇 개 있었어요. 저는 대학 내내 3점을 받은 적이 없거든요. 5점 만점에 3점은 낙제를 겨우 면한 수준인데, 대학 교무부에 찾아가 싸우지도 않았어요. 어차피 이 체제가 싫어서 탈북하려 결심한 마당에 3점이 대수냐고 생각했죠.”

“저도 졸업증에 받지 않은 3점들이 있었어요. 권력자 부모를 둔 학생들은 좋은 곳에 가기 위해 대학 교무부 직원들에게 뇌물을 주고 컴퓨터에서 점수를 바꾸었어요. 5점 최우등생과, 4점 우등생, 3점 보통생의 전체 비율을 바꿀 수 없으니 5점으로 조작하려면 누군가의 점수를 빼앗아야 했죠. 제일 힘이 없는 우리가 점수를 빼앗긴 거였죠.”

최우등을 하고도, 돈과 권력이 없으면 3점 졸업증을 받아야 했던 시대. 허 씨와 기자는 그 시대에 평양에서 대학을 다녔다. 기숙사에서 밥을 몇 숟가락만 주던 때라 대학 시절을 떠올리면 배고팠던 기억밖에 없다. 졸업증을 받은 것만으로도 기적이었다. 뇌물로 성적을 조작하고, 남의 졸업논문을 베껴 써서 제출하는 상황은 지금도 별반 나아지진 않았다.


2018년 뉴질랜드로 한 달 동안 어학연수를 떠났던 시기의 모습.


● 북한의 측량기사들
아버지가 없는 가난한 탄광마을 출신의 김책공대 졸업생에게 좋은 직업이 기다릴 리 만무했다. 북한은 직업 선택의 자유가 없다. 대학을 졸업하면 중앙에서 어디로 가라고 임명한다.
권력과 부를 가진 집안에서 태어나면 대학 때 실컷 놀고도 중앙당이나 외화벌이 업체, 보위부 등 권력기관에 발령을 받는다. 가난한 자들의 운명은 그와 반대이다.

허 씨는 2000년 3월 대학을 졸업하면서 졸업증과 함께 측량기사 자격을 부여받았다. 그리고 평양 인근 대동군 시정노동자구에 있는 중앙측량단으로 발령을 받았다. 모두가 기피하는 직업이었다.

측량기사는 20㎏이 넘는 장비를 메고 매일 같이 산을 오르내려야 했다. 1000분의 1 오차 범위 내에서 지도에 점 하나를 찍는데 사나흘이 걸렸고, 한 구역을 측량하는데 2~3개월이 걸렸다. 깊은 산속에 천막을 치고 야인생활을 하기 일쑤였다. 그나마 현장기사는 배급을 받을 수 있어 다행이었다.

북한은 측량을 하는 기관이 두 개가 있다. 하나는 중앙측량단이고, 다른 하나는 인민무력부(군) 측지국이다. 그런데 진짜 좌표는 측지국이 갖고 있다. 중앙측량단의 좌표는 일부러 정확한 좌표와 다르게 작성한다. 좌표가 고급 비밀이기 때문에 외부에 정보가 새나가면 안된다는 이유 때문이다.

허 씨는 한국에 온 뒤 큰 허탈감을 느꼈다. 위성으로 GPS를 찍는 시대를 보니 그 무거운 장비를 메고 다니며 점 하나를 찍겠다고 며칠씩 바친 과거가 너무 허망하게 생각됐기 때문이다. 북한도 2005년경부터 러시아 위성항법체계인 ‘글로나스’의 도움을 받아 위성 측량을 시도했다고는 알려졌지만, 어느 정도 활용되는지는 아직 파악되지 않고 있다.

● 원시적 석탄채굴
허 씨는 2001년 말에 온성으로 돌아왔다. 뇌물이 없으면 이직도 힘든 세상이지만, 아버지도 없는데 어머니마저 아파서 쓰러졌다고 하니 집으로 보내준 것이다. 실제로 어머니를 간호할 사람은 허 씨 밖에 없었다.

새로 발령받은 직장은 풍인탄광 기술과였다. 그러나 할 일은 없었다. 1990년대 중반 고난의 행군 시기 온성 탄광들은 모두 침수됐다. 전기가 없어 물을 빼낼 수가 없었기 때문이다. 그렇게 몇 년을 방치하다보니 갱을 다시 사용할 수가 없었다.

탄광에 다니던 사람들은 먹고 살기 위해 다른 방법을 찾았다. 일제 때 했던 방식대로 얇은 탄층 채굴을 시작한 것이다. 삽과 곡괭이로 수직굴을 파들어 가는데, 운이 좋으면 8m에서 탄층을 만나기도 하지만, 운이 나쁘면 25m까지 파들어 간다. 탄층을 만나면, 그걸 따라 이번엔 가로로 파 들어간다. 탄층의 두께는 보통 0.8~1.2m였다. 양동이를 매단 도르래를 타고 수직굴에 들어가 몸을 돌리기도 어려운 좁은 공간에서 석탄을 파서 다시 양동이로 끌어올렸다. 도무지 현대인이라고 볼 수 없는 원시적 채탄방식이었지만, 그렇게 해서라도 석탄을 캐서 팔아야 장마당에서 먹을 것을 사올 수 있었다. 이런 수직굴을 온성에선 ‘노두’라고 불렀다. 온성에는 이런 노두가 수없이 많았다. 노두당 가족, 친척, 친구 등 5~7명이 팀을 이뤄 작업했는데, 이런 사람들을 ‘노두공’이라 불렀다. 북쪽은 날씨가 춥기 때문에 먹는 것 못지않게 석탄도 귀하다. 캐내면 파는 것은 큰 문제가 안됐다.

노두도 1년 내내 할 수 있는 것이 아니었다. 땅이 어는 1~3월에만 할 수 있었고, 봄이 와서 땅이 녹으면 수직갱이 버틸 수 없기 때문에 버려야 했다. 구멍을 방치해서도 안됐다. 단속기관 사람들이 찾아와 갱을 다시 메웠는지 조사한다. 단속할 권한이 있다는 것은 뇌물을 받을 수 있다는 것을 의미하기 때문에 얼렁뚱땅 넘어가지 않는다.

온성 전체에 이런 노두가 수없이 생겨났다 사라졌다. 겨울이면 할 일이 없는 농민들도 이 일에 매달렸다. 안전은 뒷전이라 붕괴와 추락, 가스질식 등으로 죽는 사람들이 계속 생겨났지만 큰 문제가 되진 않았다. 그 일을 하지 않으면 어차피 굶어죽기 때문이다.

허 씨가 소속된 기술과는 늘 각종 공사에 동원됐다. 도로 공사, 발전소 공사 등등 인력을 차출하는 공사는 끊이질 않았다. 김책공대에서 배운 지식을 쓸 곳은 없었다.

이렇게 살다가 어느새 결혼할 나이가 됐다. 그래도 허 씨는 명색이 탄광마을이 배출한 수재이고, 평양에서 김책공대까지 나왔던 터라 여성들에게 나름 인기가 있었다.

32살 때인 2006년 그는 10살 어린 여성과 결혼했다. 아내는 탄광 선전대 가수로 나름 인기가 좋았다. 이성적인 지식인과 감성적인 예술인의 조합이었다.

그렇지만 매력과 결혼생활은 별개였다. 결혼한 직후부터 둘은 다투는 일이 많았다. 서로가 서로를 견디기 어려워했다. 4년간의 결혼생활 끝에 둘은 이혼하기로 합의했다. 어린 딸은 아내가 키우기로 했다. 이때부터 그는 중국으로 눈을 돌렸다.


2022년 인천지하철 공사 현장에서 일하고 있는 허 씨.


● 두만강을 넘나들다
강 건너 연변 왕청에는 아버지의 삼촌과 사촌 등 친척들이 살고 있었다. 국경 근처라 많은 사람들이 중국을 드나들 때도 허 씨는 명색이 김책공대 졸업생인데 조국을 배반하면 안 된다는 마음이 컸다. 하지만 이혼 후 세상이 달리 보이기 시작했다. 이혼까지 한 마당에 눈치 볼 일도, 무서울 일도 없었다.

2010년 겨울 그는 국경경비대에 돈을 쥐어주고 두만강을 넘었다. 탈북한 것은 아니고, 친척에게 도움만 받자는 목적이었다. 저녁에 넘어가서 친척에게 전화를 하고 새벽이 되기 전에 다시 북으로 넘어왔다.

2012년 2월 그는 두 번째로 중국으로 갔다. 당시는 김정일이 사망한지 얼마 안됐던 때라 경계가 매우 심했다. 그는 북한군 군복을 입고 길을 떠났다. 군인은 초소에서 잘 단속하지 않았기 때문이다. 강을 따라 난 도로로 한참을 가다가 어둠이 내릴 때 바로 두만강을 넘었다. 중국 부락의 아무 집이나 들어가 왕청 친척에게 전화를 좀 하고 싶다고 했다. 전화를 하고 몇 시간 정도 머물렀는데 갑자기 공안이 들이닥쳤다. 집주인이 그를 도와주는 척하고는 신고를 했던 것이다. 알고 보니 중국은 그즈음부터 탈북자를 신고하면 포상금을 주는 제도를 운영하고 있었다. 특히 북한군 국경경비대가 수시로 건너와 사람까지 죽이며 노략질을 했기 때문에, 중국에서 북한군은 최고의 기피대상이었다.

탈북자들이 북송 전 대기하는 도문변방수용소에 끌려갔는데 며칠 뒤 보위부에서 차를 갖고 건너와 그를 싣고 갔다.

그렇지만 그는 예상과는 달리 20일 정도 가수감됐다가 석방됐다. 서류를 보니 중국에 친척이 다 있는 것도 확실하니, 도움 좀 받으려 넘어갔을 뿐이라는 그의 말이 인정됐다. 탈북은 배반이지만, 그의 경우엔 일탈 정도로 간주됐다.

보위부라고 해봐야 어차피 한동네 사는 아는 사람들이었는데, 그들은 지역이 배출한 인재의 경력을 망가뜨리고 싶지 않았는지 그다지 혹독하게 대하진 않았다.

하지만 허 씨 입장에선 아무 것도 이루지 못하고 잡혀오니 화가 났다. 보위부 감방에서 그는 강 건너편에서 일하다 잡혀왔다는 사람을 알게 됐다. 그는 자기가 일했던 중국 훈춘의 한 슈퍼의 이름을 알려주면서, 다시 건너가 자기 이름을 대면 사장이 고용해 줄 것이라고 했다.

감방에서 나온 허 씨는 다시 두만강을 넘었다. 세 번째 탈북이었다. 그는 감옥 동기가 알려준 슈퍼로 갔다. 왕청에 가지 않은 이유는 친척들은 별로 도와줄 의향이 없어 보였기 때문이다.
슈퍼는 중국과 나진선봉을 연결하는 도로 옆에 있었는데, 두만강 건너 허 씨네 동네가 약 10㎞ 밖에 빤히 바로 보였다. 허 씨가 내륙 깊이 들어가지 않은 이유는 딸을 데려오고 싶어서였다. 고향 가까이 있어야 집과 연락이 수월하다고 판단했다. 허 씨가 일하는 슈퍼에는 북한을 오가는 운전기사들이 수시로 드나들었다. 이들을 통해 그는 전처에게 휴대전화를 전달할 수 있었다.

● 자수해 감옥에 가다
그렇게 1년쯤 지났는데 사고가 생겼다. 중국 휴대전화를 받은 전처가 그걸 이용해 돈 벌려고 브로커 일을 하다가 보위부에 체포된 것이다. 전 남편마저 실종되니 보위부는 그녀에게 한국행을 기도했다는 누명을 씌웠다.

그 소식이 허 씨에게도 전달됐다. 그래도 4년 간 살았던 정도 있고, 어린 딸까지 있으니 모르는 척 할 수가 없었다. 그는 다시 북에 나가기 위해 자수하기로 결심했다. 자신이 나타나야 전 남편이 한국에 갔다는 누명을 벗길 수 있을 것 같았다.

슈퍼 주인은 전과자 출신이었는데, 그가 북으로 가겠다고 하자 감옥에서 나오는 자기의 비법을 전수해주었다. 폐 주변에 황산철을 주사하면 고열이 나고, 염증이 생긴다면서, 자신은 그 방법으로 병원에 호송됐다가 도망쳤다고 했다. 단 이 방법의 단점은 한 달 안에 황산철을 세척하지 못하면 생명을 잃을 수도 있다고 했다.

허 씨는 그의 조언에 따라 폐에 황산철을 네 군데나 주입했다. 그리고 스스로 공안에 자수한 뒤 2014년 4월 13일 북송됐다. 그런데 이번은 보위부도 호락호락하지 않았다. 불행하게도 그가 자수한 뒤 공안이 그의 숙소를 뒤져 소지품을 북송할 때 함께 보냈던 것이다. 그 속에는 한국 영사관, 한국인 전도사 등의 전화번호가 적힌 수첩이 있었다. 이게 화근이 됐다. 고문이 시작됐다.

중국 사장이 알려준 방법은 확실히 효과가 있었다. 폐가 곪아가기 시작했던 것이다. 염증으로 심한 열까지 나 거동을 못할 정도가 됐다. 보위부는 감방에서 죽이긴 싫었는지 그를 가석방으로 집에 보냈다.

그때가 5월 말이었다. 중국 사장이 당부한 폐를 씻어야 하는 한 달이 지난 것이다. 집에 가서 이러저런 치료를 해봤지만 점점 악화됐다. 이렇게 지내다간 죽을 것 같았다. 그는 황산철 주사를 맞은 지 네 달이 지난 8월 23일 다시 중국으로 넘어왔다. 이번엔 하얼빈에 들어가 식당에 취직해 치료에만 전념했다. 하지만 몸은 점점 더 쇠약해졌다.

몸을 운신하기 어려워지자 허 씨는 죽더라도 고향에 가서 죽겠다고 생각했다. 그해 11월말 그는 다시 연길에 왔다. 연길에서 혹시나 도움을 받지 않을까 싶어 처음으로 교회에 찾아갔는데, 거기서 집도 제공하고 치료도 해주었다. 12월 말 허 씨는 산소 호흡기에 의지하는 신세가 됐다. 쇼크도 수시로 왔다. 교회에선 한국에 가서 치료를 받아야 살 수 있다며 한국행선을 주선해주었다.


교회 목회자가 될 꿈을 꾸던 당시의 허 씨. 2017년 뉴욕에서 찍은 사진이다.


● 최초로 남북 측량기사 자격 모두 획득
2015년 2월 그는 여러 탈북민들과 함께 한국으로 떠났다. 동남아 정글에서 일행을 따라갈 수 없을 때 친한 동생이 그를 업고 산을 넘었다. 우여곡절 끝에 한국에 도착했지만 다음날 적십자병원에 실려갔다. 이곳에서 4개월 동안 치료를 받다보니 하나원도 나오지 못했다.

허 씨는 인천에 거주지가 배정됐다. 건강이 너무 악화돼 일을 할 수 없는 상태라 2016년말까지 병원에 다니며 통원치료를 받았다. 하나원을 나온 다른 사람들이 하나둘 취직해 일자리를 얻는 것을 보고 조급한 마음에 노량진에서 공무원 시험을 준비하기도 했지만, 건강이 악화돼 다시 병원에 실려 가기도 했다. 한국의 의술은 역시 대단했다. 2년이라는 오랜 시간이 걸리긴 했지만, 끝내 허 씨를 완치시켰다.

치료 받는 기간에 허 씨는 목회자의 길을 걸어볼까 싶어 1년 남짓 성경공부도 했고, 화장품 회사에 취직해 일도 해봤지만 적성에 맞지 않았다.

많은 고민 끝에 북에서 배운 측량기사 일을 다시 해보려 알아보니, 남쪽도 측량기사는 일도 힘들고 보상도 적었다. 그렇지만 적성에 맞지 않는 곳에서 시간을 낭비하는 것보다는 그래도 자신있는 분야를 파보자는 생각에 2018년 한 엔지니어링 회사에 취직했다. 취직은 했어도 아무런 건설기술인 등급도 받지 못했기 때문에 회사에서 가장 많은 나이임에도 허드레 일만 해야 했다. 연봉은 2300만 원이었다. 그는 앞으로 살아가려면 자격증이 필수라는 것을 깨달았다. 어떤 자격을 갖고 있고, 어떤 경력을 쌓는가에 따라 연봉도 결정됐다.

허 씨는 회사에 다니며 1년 동안은 토목계측에 대한 용어부터 수첩에 적어 기본적인 지식을 배웠다. 그리고 이듬해 대구과학대에 입학했다. 일도 하면서 대학 공부까지 하려니 야간반을 다닐 수밖에 없었는데, 전국의 측량 관련 야간반 중에 대구가 그나마 가까웠다.

가깝다고 해도 당시 일을 하던 포항의 건설현장에서 150㎞나 떨어져 있었다. 일주일에 서너번씩 왕복 300㎞를 달려 수업을 듣고 오는 일은 결코 쉽지 않았다.

돌아오는 길에 너무 피곤해 졸음 쉼터에서 쪽잠을 자기 일쑤였다. 잠깐 눈을 붙인다는 것이 해가 중천에 걸릴 때까지 잔적도 있다.

허 씨는 대학 공부와 병행해 자격증 시험도 준비했다. 3년 동안 주경야독의 삶을 끈질기게 이어나간 끝에 그는 2022년 대학을 우수한 성적으로 졸업하고, 동시에 측량 및 지형공간정보기사와 토목기사 자격증을 받을 수 있었다. 허 씨는 남과 북에서 측량기사 자격을 각각 받은 최초의 사례다.

이러한 자격증과 경력을 인정받아 현재 허 씨는 건설기술인협회에서 고급기술인으로 인정받고 있으며, 300억 원 규모 이상의 토목공사를 책임지고 할 수 있다.


2019년 여수에서 전력 케이블용 해저터널 공사장에서 작업하는 모습. 뒷모습이 보이는 사람이 허 씨이다.


● “배워야 살 수 있다”
허 씨는 김책공대에서 무려 8년이나 공부를 했지만 여기선 모든 것을 다시 배워야 했다고 말했다.

“남쪽에 오니 용어는 물론, 장비나 자재 등 모든 것이 북한과 달랐습니다. 비유하면 북에서 통나무로 집을 짓는 법을 배웠는데, 남쪽에 오니 시멘트로 아파트를 짓는 격이죠. 그럼 집 짓는 법을 처음부터 다시 배워야하죠. 물론 북한 김책공대 과정이 전혀 의미 없는 것은 아닙니다. 북한에선 가장 기본적인 것, 즉 공부하는 방법을 배운 것 같습니다.”

그는 남북은 통합성에서도 차이가 크다고 했다.

“여기는 한 가지를 하려면 열 가지를 알아야 합니다. 많은 것들이 서로 연결돼 있어 전체적으로 진행되죠. 반면 북한은 직무가 매우 세분화돼 있고, 맡겨진 것만 하면 됐어요.”

자격증과 경력을 쌓고 나니 연봉도 빠르게 올라갔다. 김책공대까지 입학했던 북한 시골 수재가 다시 자신의 두뇌와 재능을 발휘하는 데는 오랜 시간이 걸리지 않았다. 2300만 원에서 시작했던 연봉은 6년 만에 3배 이상 높아졌다.

그는 여기에 만족하지 않았다. 그는 올해 3월 다시 대구대 공간정보전문기술 석사과정에 입학했다. 토질 및 기초기술사 자격을 취득하기 위해서다. 다른 자격증과는 달리 이 자격은 받기가 매우 어렵다. 허 씨의 계획은 향후 5년 안에 석사와 함께 기술사 자격을 획득하는 것이다.

그렇다고 공부만 할 수는 없는 일. 요즘 허 씨는 마산만에서 스팀배관 부설을 위한 해저터널을 뚫는 작업을 하고 있다. 그의 직책은 공사차장. 터널 시공 품질을 총괄하는 중요한 자리다.

건설 현장은 매우 거칠고 다툼도 많다. 외국인 근로자들도 많아 의사소통의 문제도 많다. 많은 어려움이 있지만 허 씨는 포기하지 않고 한 걸음씩 나가고 있다.

“거친 현장이라서 그런지 북에서 왔다고 우습게 보는 사람들이 많아요. 아직도 저는 ‘나는 여전히 이방인이구나’라는 생각을 하고 있습니다. 그렇지만 실력은 남에게 뒤진다고 생각하지 않습니다. 여러 곳에서 이직 제안도 많이 받습니다.”

2023년 남북하나재단이 주관한 정착사례 발표대회에서 그는 최우수상인 통일부 장관상을 받았다. 하지만 허 씨는 지금은 정착의 첫 발자국을 뗀 것에 불과하다고 했다.

그는 자신의 이름으로 회사를 만들어 키우는 것을 다음 목표로 정했다. 그 목표가 달성되면 또 할 일이 있다. 나아가 통일이 되면 할 계획도 미리 생각해두었다.

“저는 북에 돌아가 여기서 배운 기술을 북에 전수할 겁니다. 한국은 토목 공사를 할 때 측량, 시공, 품질까지 다 알아야 합니다. 통일 되면 교통인프라를 다시 정리해야 할 것인데, 북한에서 대학을 다녔던 동창들은 통합성에 있어 크게 떨어집니다. 이런 것을 가르쳐야죠. 그리고 남북에서 모두 측량기사 자격을 받은 유일한 사람이니 다른 꿈도 있습니다. 남북공간정보 통합지도체계를 만드는 것도 중요한 목표입니다.”

꿈을 말할 때 그는 가장 행복한 표정이었다.'''

# 언어모델 설정
llm = BedrockChat(model_kwargs={"temperature": 0},
                        model_id="anthropic.claude-v2",
                        client=bedrock
                    )
# 프롬프트 설정
prompt = PromptTemplate(
    template="""백틱으로 둘러싸인 전사본을 이용해 해당 유튜브 비디오를 요약해주세요. \
    ```{text}```
    """, input_variables=["text"]
)
combine_prompt = PromptTemplate(
    template="""Combine all the youtube video transcripts provided within backticks \
    ```{text}```
    Provide a concise summary between 5 to 10 sentences.
    """, input_variables=["text"]
)
# LangChain을 활용하여 긴 글 요약하기
# 글 쪼개기
text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=0)
texts = text_splitter.create_documents([script])
# 요약하기
chain = load_summarize_chain(llm, chain_type="map_reduce", verbose=False,
                            map_prompt=prompt, combine_prompt=combine_prompt)
summerize = chain.run(texts)
# 최종 출력
print(summerize)