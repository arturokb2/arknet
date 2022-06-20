
var app_update = new Vue({
    el:'#update_pers',
    data:{
        v_update:false,
        v_ok:false
    },
    methods:{
        update_pers:function(){
            let file = document.getElementById("update_pers_file")
            if (file.files.length != 0 ){
                let url = window.location.host+'/update_pers_file_hospital/'
                let formData = new FormData()
                for (f of file.files){
                    formData.append('files',f)
                }

                fetch('/update_pers_file_hospital/', {
                    method: 'POST',
                    body: formData,
                    headers: {
                        "X-CSRFToken": (document.cookie).split("=")[1]
                    }
                })
                    .then(response => response.json())
                    .then(data => {
                        this.v_update = true
                    })
            }
            else{
                console.log('Файлы не выбран')
            }
          },
    }
})