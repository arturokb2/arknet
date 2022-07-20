// $(".date").mask("99.99.9999")

Vue.component('date', {
  template: `<div class="text-center">
      <div><label>за период (дд.мм.гггг)</label></div>
      <label>с</label>
      <input type="date" id="date_r_1">
      <label>по</label>
      <input type="date" id="date_r_2">
      </div>`
})

let create_reestr_d = new Vue({
  el: '#create_reestr_div',
  data: {
    create_res:false,
    end:false,
    progress:false,
    progress_bar:0,
  },
  methods: {
    create_reestr: function () {
      var formData = new FormData()
      let date_1 = document.getElementById("date_r_1_create")
      let date_2 = document.getElementById("date_r_2_create")
      let type_res = document.getElementById("sl_res")
      let his = document.getElementById("his")
      formData.append('type', 'create_reestr')
      formData.append('date_1', date_1.value)
      formData.append('date_2', date_2.value)
      formData.append('type_res',type_res.value)
      formData.append("his", his.value)
      $('#download_reestr').empty()
      
      if (date_1.value != '' && date_2.value != ''){
        var r = sendRequest('create_reestr/', 'post', formData)
        .then(response => {
          this.create_res = true
          this.end =false
          this.progress_bar = 0
          this.progress = true

          let progress = document.getElementById("progress")
          progress.setAttribute("style", "width:" + 0 + "%")
          progress.innerText = 0 + '%'
        })
        .catch(error => {
        })
      }
    },
    close:function(){
      this.create_res =false
      this.end = false
      this.progress_bar = 0
      this.progress = false
      let progress = document.getElementById("progress")
      if (progress != undefined){
        this.progress_bar = 0
        progress.setAttribute("style", "width:" + 0 + "%")
        progress.innerText = 0 + '%'
      }
    }
  }
})




// create_reestr.onclick = function(event){

//   var formData = new FormData()
//   var date_1 = document.getElementById("date_1")
//   var date_2 = document.getElementById("date_2")
//   formData.append('type', 'create_reestr')
//   formData.append('date_1',date_1.value)
//   formData.append('date_2',date_2.value)
//   console.log('qwe')

//   var r = sendRequest('create_reestr/', 'post', formData)
//   .then(response => {
//   })
//   .catch(error => {
//   })
// }

// function create_reestr(){
//   var formData = new FormData()
//   var date_1 = document.getElementById("date_r_1")
//   var date_2 = document.getElementById("date_r_2")
//   formData.append('type', 'create_reestr')
//   formData.append('date_1',date_1.value)
//   formData.append('date_2',date_2.value)
//   console.log('create_reestr')

//   // var r = sendRequest('create_reestr/', 'post', formData)
//   // .then(response => {
//   // })
//   // .catch(error => {
//   // })
// }