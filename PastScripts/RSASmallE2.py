import gmpy
from Crypto.Util.number import long_to_bytes

# low public exponent attack

n= 20948184905072216948549865445605798631663501453911333956435737119029531982149517142273321144075961800694876109056203145122426451759388059831044529163118093342195028080582365702020138256379699270302368673086923715628087508705525518656689253472590622223905341942685751355443776992006890500774938631896675247850244098414397183590972496171655304801215957299268404242039713841456437577844606152809639584428764129318729971500384064454823140992681760685982999247885351122505154646928804561614506313946302901152432476414517575301827992421830229939161942896560958118364164451179787855749084154517490249401036072261469298158281
c = 747861028284745583986165203504322648396510749839398405070811323707600711491863944680330526354962376022146478962637944671170833980881833864618493670661754856280282476606632288562133960228178540799118953209069757642578754327847269832940273765635707176669208611276095564465950147643941533690293945372328223742576232667549253123094054598941291288949397775419176103429124455420699502573739842580940268711628697334920678442711510187864949808113210697096786732976916002133678253353848775265650016864896187184151924272716863071499925744529203583206734774883138969347565787210674308042083803787880001925683349235960512445949
e = 3

m = gmpy.root(c, 3)[0]
print(long_to_bytes(m))
