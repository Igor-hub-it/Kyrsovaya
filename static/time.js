function liveTime() {   
    let live_time = new Date().toLocaleString()
    time.textContent = 'Сейчас: ' + live_time/*.slice(live_time.indexOf(',') + 2)*/
}

const time = document.querySelector('.first_block .date')
setInterval(liveTime, 1000)
