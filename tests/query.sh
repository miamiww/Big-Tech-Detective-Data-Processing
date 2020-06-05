
TEST_QUERY(){
    COMPANY=$1
    RIR=$2

    whois -h whois.$RIR.net $COMPANY | grep ^inet | while read -r ip; do
        ip=${ip//[[:blank:]]/}
        ip=${ip#"inetnum"}
        ip=${ip#"inet6num"}
        ip=${ip#":"}
        ip=${ip//[[:blank:]]/}
        echo $ip
    done
}
TEST_QUERY "Amazon" "ripe"