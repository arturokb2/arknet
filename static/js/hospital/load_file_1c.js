// function sendRequest(url,method,data){
//   var r = axios({
//     method:method,
//     url:url,
//     data:data,
//     xsrfCookieName:'csrftoken',
//     xsrfHeaderName:'X-CSRFToken',
//     headers:{
//       'X-Requested-With':'XMLHttpRequest'
//     }
//   })
//   return r
// }

var app = new Vue({
  el: '#app',
  data: {
    message: '',
    oper: '',
    sluch: '',
    sluch_10: '',
    user: '',
    mes_div: null,
    loader_mse: null,
    loader_sp: null,
    loader_sp_end: null,
    err_oper: null,
    err_sluch: null,
    loader_sp_st: null,
    progress_bar: 0,
    exportfrom1_loading: false,
    exportfrom1_completed: false,
    div_progress: false,

  },
  created: function () {
    var formData = new FormData()
    formData.append('type', 'get_user')
    var r = sendRequest('', 'post', formData)
      .then(response => {
        this.user = response.data.user
      })
  },
  methods: {
    load_files() {
      this.mes_div = null
      this.loader_mse = false
      this.loader_sp = null
      this.err_oper = null
      this.err_sluch = null
      var formData = new FormData()
      const oper_ = document.getElementById('file_oper')
      const sluch_ = document.getElementById('file_sluch')
      const sluch_10_ = document.getElementById('file_sluch_10')

      this.message = 'Записи обрабатываются'

      // if (oper_.files[0] === undefined || sluch_.files[0] === undefined) {
      //   this.message = 'Файлы не загружены'
      //   this.mes_div = false
      // }
      // else if (oper_.files[0].name != 'OPER.DBF'){
      //   this.mes_div = false
      //   this.err_oper = true
      // }
      // else if (sluch_.files[0].name != 'SLUCH.DBF'){
      //   this.mes_div = false
      //   this.err_sluch = true
      // }

      // else {

      let err_oper = true
      let err_sluch_ = true
      let err_sluch_10_ = true

      if (oper_.files.length != 0) {
        if (oper_.files[0].name != 'OPER.DBF') {
          this.message = 'Ошибка выбора файла'
          err_oper = false
        }
      }
      if (sluch_.files.length != 0) {
        if ((sluch_.files[0].name != 'SLUCH.DBF')) {
          this.message = 'Ошибка выбора файла'
          err_sluch_ = false
        }
      }
      if (sluch_10_.files.length != 0) {
        if ((sluch_10_.files[0].name == 'SLUCH.DBF') || (sluch_10_.files[0].name == 'MANIP.DBF') || (sluch_10_.files[0].name == 'OPER.DBF')
          || (sluch_10_.files[0].name == 'OSL.DBF') || (sluch_10_.files[0].name == 'Perevod.DBF') || (sluch_10_.files[0].name == 'PREDSTAV.DBF')) {
          this.message = 'Ошибка выбора файла'
          err_sluch_10_ = false
        }
      }

      if (err_oper == err_sluch_ == err_sluch_10_) {
        this.message = 'обработка данных'
        formData.append('oper', oper_.files[0])
        formData.append('sluch', sluch_.files[0])
        formData.append('sluch_10', sluch_10_.files[0])
        formData.append('user', this.user)
        formData.append('type', 'load_fales')
        var r = sendRequest('', 'post', formData)
          .then(response => {
            this.message = 'Записи обрабатываются'
            this.exportfrom1_loading = false
            this.exportfrom1_completed = false
            this.err_oper = false
            this.err_sluch = false
            this.div_progress = false
            this.progress_bar = 0
            this.exportfrom1_loading = true
            this.div_progress = true

            let progress = document.getElementById("progress")
            progress.setAttribute("style", "width:" + this.progress_bar + "%")
            progress.innerText = this.progress_bar + '%'

          })
          .catch(error => {

          })
      }

      // }  


      // else{
      //   this.message = 'обработка данных'
      // formData.append('oper', oper_.files[0])
      // formData.append('sluch', sluch_.files[0])
      // formData.append('sluch_10', sluch_10_.files[0])
      // formData.append('user', this.user)
      // formData.append('type', 'load_fales')
      // var r = sendRequest('', 'post', formData)
      //   .then(response => {
      //     this.message = 'Записи обрабатываются'
      //     this.exportfrom1_loading = false
      //     this.exportfrom1_completed = false
      //     this.err_oper = false
      //     this.err_sluch = false
      //     this.div_progress = false
      //     this.progress_bar = 0
      //     this.exportfrom1_loading = true
      //     this.div_progress = true

      //     let progress = document.getElementById("progress")
      //     progress.setAttribute("style", "width:" + this.progress_bar + "%")
      //     progress.innerText = this.progress_bar + '%'

      //   })
      //   .catch(error => {

      //   }) 
      // }
      // }
    },
    close() {
      this.exportfrom1_loading = false
      this.exportfrom1_completed = false
      this.err_sluch = false
      this.err_oper = false
      this.div_progress = false
      this.progress_bar = 0

      let progress = document.getElementById("progress")
      progress.setAttribute("style", "width:" + this.progress_bar + "%")
      progress.innerText = this.progress_bar + '%'
    }


  }

})
