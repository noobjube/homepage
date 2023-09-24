function pihole(){
    let hostname = location.hostname
    location.replace("http://"+hostname+"/admin")
}