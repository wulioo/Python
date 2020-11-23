#! bin/bash

kuai="kuai500-release"
path="../FAQ/index.html"
url=""
#cp ./kuai500-*.* bak/ && mv ./kuai500-*.* ${kuai}-$1.zip
#ossutilmac64 cp -rf ./${kuai}-$1.zip oss://k500app/release/

sed -n 's/release-[0-9].[0-9].[0-9]\{2\}/release-'$1'/p' ${path}
scp -r ./index.html root@159.138.133.209:/www/wwwroot/${url}

