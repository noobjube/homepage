function pihole(){
    let hostname = location.hostname
    location.replace("http://"+hostname+"/admin")
}
function startpc(){
    let hostname = location.hostname
    location.replace("http://"+hostname+":5000/wakepc")
}