aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventSource,AttributeValue=signin.amazonaws.com


aws cloudtrail lookup-events \
    --lookup-attributes AttributeKey=EventName,AttributeValue=GetCallerIdentity \
    --start-time "$(date -u -v-1H '+%Y-%m-%dT%H:%M:%SZ')" \
    --end-time "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"


aws cloudtrail lookup-events \
    --lookup-attributes AttributeKey=EventName,AttributeValue=GetCallerIdentity \
    --start-time "$(date -u --date='1 hour ago' +'%Y-%m-%dT%H:%M:%SZ')" \
    --end-time "$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
