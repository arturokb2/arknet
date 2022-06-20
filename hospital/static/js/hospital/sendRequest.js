function sendRequest(url,method,data){
    var r = axios({
      method:method,
      url:url,
      timeout: 1000 * 900,
      data:data,
      xsrfCookieName:'csrftoken',
      xsrfHeaderName:'X-CSRFToken',
      headers:{
        'X-Requested-With':'XMLHttpRequest'
      }
    })
    return r
  }
// function sendRequest(url,method,data){
//   let r = await fetch(url,{
//     method:method,
//     body:data
//   })
// }
