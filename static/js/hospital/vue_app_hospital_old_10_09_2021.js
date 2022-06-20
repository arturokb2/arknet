//Спровочники
var Next = null

let app = new Vue({
    el: '#app_hospital',
    data: {
        // list_w: [],
        // list_otde: [],
        // list_rab_ner: [],
        // list_in_t: [],
        // list_lpu: [],
        // list_vrez: [],
        // list_oksm: [],
        // list_v012: [],
        // list_v009: [],
        // list_v020: [],
        // list_vra: [],
        // pr_osob: [],
        // list_v001: [],
        // list_t006: [],
        // list_ab_obsh: [],
        // list_pope: [],
        // list_prli: [],
        // list_trv: [],
        // list_isfin: [],
        // list_skom: [],
        // list_f008: [],
        // list_f011: [],
        // list_n018: [],
        // list_n007: [],
        // list_n010: [],
        // list_n008: [],
        // list_n011: [],
        // list_n019: [],
        // list_n013: [],
        // list_n014: [],
        // list_n001: [],
        // list_v028: [],
        // list_v029: [],
        // list_v014: [],
        // list_prpg: [],
        // list_per: [],
        // list_pr_per: [],
        // list_tip_pb: [],
        // list_m_prer: [],
        // list_v027: [],
        // list_trvnas: [],
        // list_anesthesia: [],
        list_ds: Array(),


        sprav_list: [],



        // Поиск записей истории
        check_history: true,
        search_history: '',
        check_response_history: false,
        response_history: [],
        //Получаем данные из истории
        history: '',
        //Навигация
        inf_pers_info: false,
        inf_diagnoses: false,
        inf_koyko: false,
        inf_operation: false,
        inf_ks_zabolev: false,
        inf_complication: false,
        inf_work_capacity: false,
        inf_manipulation: false,
        inf_translations: false,
        inf_post_mortem: false,
        inf_injury: false,
        inf_policy_passport_snills: false,
        inf_pregnancy: false,
        inf_disability: false,
        inf_patient_p: false,
        inf_address: false,
        //отбражать при определенных условиях
        inf_onmk: false,
        inf_onmk_sp: false,
        inf_onmk_li: false,

        inf_onk: false,
        inf_mo: false,

        protoc: false,
        // Побочные поля
        ASCII: {
            "й": "Q", "ц": "W", "у": "E", "к": "R", "е": "T",
            "н": "Y", "г": "U", "ш": "I", "щ": "O",
            "з": "P", "ф": "A", "ы": "S", "в": "D", "а": "F",
            "п": "G", "р": "H", "о": "J", "л": "K", "д": "L",
            "я": "Z", "ч": "X", "с": "C", "м": "V", "и": "B",
            "т": "N", "ь": "M"
        },
        ds_naim: '',



    },
    mounted: function () {
        this.get_sprav_list()
    },
    methods: {
        get_sprav_list: function () {
            let query = `
          query{
              V005{
                polname
              },
              Otde{
                naim
              },
              RabNer{
                naim
              },
              T004{
                name
              },
              F003{
                naim
              },
              V014{
                tipName
              },
              Prpg{
                naim
              },
              Vrzb{
                naim
              },
              PER{
                naim
              },
              V012{
                idIz
                izName
               },
              V009{
                idTip
                tipName
               },
              V020{
                kPrname
              },
              Vra{
                kod
              },
              PROsob{
                  kod
                  naim
              },
              V001{
                 kod
              },
              anesthesia{
                kod
              },
              T006{
                codeUslKz
              },
              Pope{
                kod
              },
              AbObsh{
                kod
              },
              PRPer{
                naim
              },
              Prli{
                kod
              },
              Trv{
                 naim
              },
              Trvnas{
                 naim
              },
              Isfin{
                 naim
              },
              Skom{
                 naim
              },
              F008{
                tipName
              },
              F011{
                docname
              },
              TipPb{
                naim
              },
              MetPb{
                naim
               },
              Oksm{
                naim
               },
               N007{
                mrfName
               },
               N010{
                kodIgh
               },
               N008{
                rMName
               },
               N011{
                rIName
               },
               N018{
                reasName
               },
               V027{
                nCz
               },
               N019{
                consName
               },
               N013{
                tlechName
               },
               N014{
                thirName
               },
               N001{
                protName
               },
               V028{
                nVn
               },
               V029{
                nMet
               }
               
          }`
            return fetch('graph_hospital/', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query })
            })
                .then(response => response.json())
                .then(data => {
                    this.sprav_list = data.data


                    // return data
                })
                .catch((e) => {
                    // console.log(e)
                })
        },
        get_history: function () {
            this.check_history = true
            if (this.search_history != '') {
                var formData = new FormData()
                formData.append('history', this.search_history)
                formData.append('type', 'search')
                var r = sendRequest('', 'post', formData)
                    .then(response => {
                        this.check_response_history = true
                        this.response_history = response.data.rez
                    })
                    .catch(error => {
                        this.check_response_history = false
                    })
            }
            else {
                this.check_history = false
            }
        },
        get_data_cards: function (id) {

            var formData = new FormData()
            formData.append('id', id)
            formData.append('type', 'data_history')
            var r = sendRequest('', 'post', formData)
                .then(response => {
                    this.inf_pers_info = true
                    var med_card_menu = document.getElementById("med_card_menu")
                    for (let menu of med_card_menu.querySelectorAll('a')) {
                        menu.classList.remove("active")
                    }
                    // var med_card_menu = document.getElementById("med_card_menu")
                    med_card_menu.childNodes[0].classList.add("active")
                    document.getElementById("list-profile-list_inf_post_mortem").classList.add("disabled")
                    document.getElementById("list-profile-list_inf_pregnancy").classList.add("disabled")
                    document.getElementById("list-profile-list_inf_onmk").classList.add("disabled")
                    document.getElementById("list-profile-list_inf_onk").classList.add("disabled")

                    this.history = response.data.rez

                    var otd = this.history.otd
                    var dskz = this.history.dskz.kod
                    // var res = this.history.rslt
                    var res = $('#rslt').val()
                    var otde = ['НЕВРОЛОГИЯ N1', 'НЕВРОЛОГИЯ N2', 'НЕВРОЛОГИЯ N3']
                    var resl = ['Умер 105', 'Умер в приёмном покое 106']
                    var ds = ['G45', 'G46', 'I60', 'I60.0', 'I60.1', 'I60.2', 'I60.3', 'I60.4', 'I60.5',
                        'I60.6', 'I60.7', 'I60.8', 'I60.9', 'I61', 'I61.0', 'I61.1', 'I61.2', 'I61.3',
                        'I61.4', 'I61.5', 'I61.6', 'I61.8', 'I61.9', 'I62', 'I62.0', 'I62.1', 'I62.9',
                        'I63', 'I63.0', 'I63.1', 'I63.2', 'I63.3', 'I63.4', 'I63.5', 'I63.6', 'I63.8', 'I63.9']


                    // if (resl.indexOf(res) != -1) {
                    //     document.getElementById("list-profile-list_inf_post_mortem").classList.remove("disabled")
                    //     }
                    // else {
                    //     document.getElementById("list-profile-list_inf_post_mortem").classList.add("disabled")
                    // }

                    // if (this.history.dskz.kod[0] == 'O'){
                    //     document.getElementById("list-profile-list_inf_post_mortem").classList.remove("disabled")
                    // }
                    // else {
                    //     document.getElementById("list-profile-list_inf_post_mortem").classList.add("disabled")
                    // }

                    if ((otde.indexOf(otd) != -1) && (ds.indexOf(dskz) != -1)) {
                        document.getElementById("list-profile-list_inf_onmk").classList.remove("disabled")
                        this.inf_onmk_sp = true
                        if (resl.indexOf(res) != -1) {
                            this.inf_onmk_li = true
                        }
                        else {
                            this.inf_onmk_li = false
                        }
                    }
                    else {
                        document.getElementById("list-profile-list_inf_onmk").classList.add("disabled")
                        this.inf_onmk_sp = false
                        this.inf_onmk_li = false
                    }

                    if (response.data.rez.dskz.kod[0] == 'C') {
                        document.getElementById("list-profile-list_inf_onk").classList.remove("disabled")
                    }
                    else {
                        document.getElementById("list-profile-list_inf_onk").classList.add("disabled")
                    }

                    Next = null

                    document.getElementById("list-home-list_inf_pers_info").click()



                })
                .catch(error => {
                    this.history = []
                })

        },
        rec_list_ds: function (kod, $event) {
            if (kod.length == 1) {
                kod = this.ASCII[event.data]
                if (kod != undefined) {
                    let id = event.target.id
                    if (id == 'dsny_kod') {
                        this.history.dsny.kod = kod
                    }
                    else if (id == 'ds_0_kod') {
                        this.history.ds_0.kod = kod
                    }
                    else if (id == 'dsk_kod') {
                        this.history.dsk.kod = kod
                    }
                    else if (id == 'dskz_kod') {
                        this.history.dskz.kod = kod

                        if (kod[0] == 'C') {
                            document.getElementById("list-profile-list_inf_onk").classList.remove("disabled")
                        }
                        else {
                            document.getElementById("list-profile-list_inf_onk").classList.add("disabled")
                        }

                        if (kod[0] == 'O') {
                            document.getElementById("list-profile-list_inf_pregnancy").classList.remove("disabled")
                        }
                        else {
                            document.getElementById("list-profile-list_inf_pregnancy").classList.add("disabled")
                        }

                    }
                    else if (id == 'ds_osl_kod') {
                        this.history.ds_osl.kod = kod
                    }
                    else if (id == 'dsc_kod') {
                        this.history.dsc.kod = kod
                    }
                    else if (id == 'dson_kod') {
                        this.history.dson.kod = kod
                    }

                    else if (id == 'ds_let_kod') {
                        this.history.ds_let.kod = kod
                    }
                    else if (id == 'dspat_kod') {
                        this.history.dspat.kod = kod
                    }
                    else if (id == 'details_kod') {
                        this.history.details.kod = kod
                    }
                }

            }
            let query = `
          query{
              DsList(ds:"${kod}"){
                kod
              }
          }`
            fetch('graph_hospital/', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query })
            })
                .then(response => response.json())
                .then(data => {
                    let ds = []
                    data.data.DsList.forEach(function (data) {
                        ds.push(data.kod)
                    })
                    this.list_ds = ds

                })
                .catch((e) => {
                    // console.log(e)
                })

        },
        rec_ds_naim: function (kod, $event) {
            this.ds_naim = ''
            let id = event.target.id
            let query = `
              query{
                  DsName(ds:"${kod}"){
                    naim
                  }
              }`
            fetch('graph_hospital/', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query })
            })
                .then(response => response.json())
                .then(data => {

                    if (id == 'dsny_kod') {
                        this.history.dsny.naim = data.data.DsName[0].naim
                    }
                    else if (id == 'ds_0_kod') {
                        this.history.ds_0.naim = data.data.DsName[0].naim
                    }
                    else if (id == 'dsk_kod') {
                        this.history.dsk.naim = data.data.DsName[0].naim
                    }
                    else if (id == 'dskz_kod') {
                        this.history.dskz.naim = data.data.DsName[0].naim
                    }
                    else if (id == 'ds_osl_kod') {
                        this.history.ds_osl.naim = data.data.DsName[0].naim
                    }
                    else if (id == 'dsc_kod') {
                        this.history.dsc.naim = data.data.DsName[0].naim
                    }
                    else if (id == 'dson_kod') {
                        this.history.dson.naim = data.data.DsName[0].naim
                    }
                    else if (id == 'ds_let_kod') {
                        this.history.ds_let.naim = data.data.DsName[0].naim
                    }
                    else if (id == 'dspat_kod') {
                        this.history.dspat.naim = data.data.DsName[0].naim
                    }
                    else if (id == 'details_kod') {
                        this.history.details.naim = data.data.DsName[0].naim
                    }

                })
                .catch((e) => {
                    // console.log(e)
                })
        },
        default_temp: function () {
            this.inf_pers_info = false
            this.inf_diagnoses = false
            this.inf_koyko = false
            this.inf_operation = false
            this.inf_ks_zabolev = false
            this.inf_complication = false
            this.inf_work_capacity = false
            this.inf_manipulation = false
            this.inf_translations = false
            this.inf_post_mortem = false
            this.inf_injury = false
            this.inf_policy_passport_snills = false
            this.inf_pregnancy = false
            this.inf_disability = false
            this.inf_patient_p = false
            this.inf_address = false
            this.inf_onmk = false
            this.inf_onk = false
            this.inf_mo = false
        }
    }
})






function Get_data_cards() {

    let id = this.event.target.getAttribute("id")

    app.get_data_cards(id)

    setTimeout(() => {
        post_mortem_disabled()
        if ($('#dskz_kod').val()[0] == 'O') {
            document.getElementById("list-profile-list_inf_pregnancy").classList.remove("disabled")
        }
        else {
            document.getElementById("list-profile-list_inf_pregnancy").classList.add("disabled")
        }

        if ($('#dskz_kod').val()[0] == 'C') {
            document.getElementById("list-profile-list_inf_onk").classList.remove("disabled")
        }
        else {
            document.getElementById("list-profile-list_inf_onk").classList.add("disabled")
        }

        var an_rem = document.getElementById("an_rem")
        // console.log(app.$data.history.le_vr)
        if (app.$data.history.le_vr['aro'] != null && app.$data.history.le_vr['aro'].length > 0) {
            an_rem.setAttribute('style', 'border:1px solid')
        }
        else {
            an_rem.setAttribute('style', 'display:none')
        }

        onmk_disabled()
    }, 300)

}

function Select_trs() {
    let trs_radio = document.getElementById("Trs").getElementsByClassName("form-group form-check")
    for (let trs in trs_radio) {
        try {
            trs_radio[trs].childNodes[0].checked = false
        }
        catch (err) {
        }
    }

    if (app.$data.history.trs != null) {
        var v_trs = app.$data.history.trs
    }
    else {
        var v_trs = ''
    }
    for (let trs in trs_radio) {
        try {
            let label = trs_radio[trs].getElementsByTagName("label")
            label[0].onclick = function () {
                app.$data.history.trs = trs_radio[trs].textContent.replace(/\s+/g, ' ').trim()
            }


            if (trs_radio[trs].textContent.replace(/\s+/g, ' ').trim() == v_trs) {
                trs_radio[trs].childNodes[0].checked = true
            }
        }
        catch (err) {
        }
    }
}
function onmk_disabled() {
    var otd = $("#otd").val()
    var dskz = $("#dskz_kod").val()
    var res = $("#rslt").val()
    var otde = ['НЕВРОЛОГИЯ N1', 'НЕВРОЛОГИЯ N2', 'НЕВРОЛОГИЯ N3']
    var ds = ['G45', 'G46', 'I60', 'I60.0', 'I60.1', 'I60.2', 'I60.3', 'I60.4', 'I60.5',
        'I60.6', 'I60.7', 'I60.8', 'I60.9', 'I61', 'I61.0', 'I61.1', 'I61.2', 'I61.3',
        'I61.4', 'I61.5', 'I61.6', 'I61.8', 'I61.9', 'I62', 'I62.0', 'I62.1', 'I62.9',
        'I63', 'I63.0', 'I63.1', 'I63.2', 'I63.3', 'I63.4', 'I63.5', 'I63.6', 'I63.8', 'I63.9']
    var resl = ['Умер 105', 'Умер в приёмном покое 106']

    if ((otde.indexOf(otd) != -1) && (ds.indexOf(dskz) != -1)) {
        document.getElementById("list-profile-list_inf_onmk").classList.remove("disabled")
        app.$data.inf_onmk_sp = true
        if (resl.indexOf(res) != -1) {
            app.$data.inf_onmk_li = true
        }
        else {
            app.$data.inf_onmk_li = false
        }
    }
    else {
        document.getElementById("list-profile-list_inf_onmk").classList.add("disabled")
        app.$data.inf_onmk_sp = false
    }
}
function post_mortem_disabled() {
    var resl = ['Умер 105', 'Умер в приёмном покое 106']
    var res = $("#rslt").val()
    if (resl.indexOf(res) != -1) {
        document.getElementById("list-profile-list_inf_post_mortem").classList.remove("disabled")
    }
    else {
        document.getElementById("list-profile-list_inf_post_mortem").classList.add("disabled")
    }
}
function onmk() {
    Onmk_sp_u()
    Onmk_li_u()
}

function Onmk_sp_u() {
    //При открытии считываем 
    //Object(history.onmk_sp).p001
    //Изменеия по клику
    $('input[name="p001_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p001 = event.target.getAttribute('n')
    })
    $('input[name="p002_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p002 = event.target.getAttribute('n')
    })
    $('input[name="p003_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p003 = event.target.getAttribute('n')
    })
    $('input[name="p004_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p004 = event.target.getAttribute('n')
    })
    $('input[name="p005_1_sp"]').click(function (event) {

        app.$data.history.onmk_sp.p005_1 = event.target.getAttribute('n')
    })
    $('input[name="p005_2_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p005_2 = event.target.getAttribute('n')
    })
    $('input[name="p006_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p006 = event.target.getAttribute('n')
    })
    $('input[name="p007_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p007 = event.target.getAttribute('n')
    })
    $('input[name="p008_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p008 = event.target.getAttribute('n')
    })
    $('input[name="p009_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p009 = event.target.getAttribute('n')
    })
    $('input[name="p010_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p010 = event.target.getAttribute('n')
    })
    $('input[name="p011_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p011 = event.target.getAttribute('n')
    })
    $('input[name="p012_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p012 = event.target.getAttribute('n')
    })
    $('input[name="p013_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p013 = event.target.getAttribute('n')
    })
    $('input[name="p014_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p014 = event.target.getAttribute('n')
    })
    $('input[name="p015_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p015 = event.target.getAttribute('n')
    })
    $('input[name="p016_sp"]').click(function (event) {
        app.$data.history.onmk_sp.p016 = event.target.getAttribute('n')
    })



}

function Onmk_li_u() {

    //Измениния по клику
    //Object(history.onmk_li).p001
    $('input[name="p001_li"]').click(function (event) {
        app.$data.history.onmk_li.p001 = event.target.getAttribute('n')
    })
    $('input[name="p002_li"]').click(function (event) {
        app.$data.history.onmk_li.p002 = event.target.getAttribute('n')
    })
    $('input[name="p003_li"]').click(function (event) {
        app.$data.history.onmk_li.p003 = event.target.getAttribute('n')
    })
    $('input[name="p004_li"]').click(function (event) {
        app.$data.history.onmk_li.p004 = event.target.getAttribute('n')
    })
    $('input[name="p005_li"]').click(function (event) {
        app.$data.history.onmk_li.p005 = event.target.getAttribute('n')
    })
    $('input[name="p006_li"]').click(function (event) {
        app.$data.history.onmk_li.p006 = event.target.getAttribute('n')
    })
    $('input[name="p007_li"]').click(function (event) {
        app.$data.history.onmk_li.p007 = event.target.getAttribute('n')
    })
    $('input[name="p008_li"]').click(function (event) {
        app.$data.history.onmk_li.p008 = event.target.getAttribute('n')
    })
    $('input[name="p009_li"]').click(function (event) {
        app.$data.history.onmk_li.p009 = event.target.getAttribute('n')
    })
    $('input[name="p010_li"]').click(function (event) {
        app.$data.history.onmk_li.p010 = event.target.getAttribute('n')
    })
    $('input[name="p011_li"]').click(function (event) {
        app.$data.history.onmk_li.p011 = event.target.getAttribute('n')
    })
    $('input[name="p012_li"]').click(function (event) {
        app.$data.history.onmk_li.p012 = event.target.getAttribute('n')
    })
    $('input[name="p013_li"]').click(function (event) {
        app.$data.history.onmk_li.p013 = event.target.getAttribute('n')
    })
    $('input[name="p014_li"]').click(function (event) {
        app.$data.history.onmk_li.p014 = event.target.getAttribute('n')
    })
    $('input[name="p015_li"]').click(function (event) {
        app.$data.history.onmk_li.p015 = event.target.getAttribute('n')
    })
    $('input[name="p016_li"]').click(function (event) {
        app.$data.history.onmk_li.p016 = event.target.getAttribute('n')
    })
    $('input[name="p017_li"]').click(function (event) {
        app.$data.history.onmk_li.p017 = event.target.getAttribute('n')
    })
    $('input[name="p018_li"]').click(function (event) {
        app.$data.history.onmk_li.p018 = event.target.getAttribute('n')
    })
    $('input[name="p019_li"]').click(function (event) {
        app.$data.history.onmk_li.p019 = event.target.getAttribute('n')
    })
    $('input[name="p020_li"]').click(function (event) {
        app.$data.history.onmk_li.p020 = event.target.getAttribute('n')
    })
    $('input[name="p021_li"]').click(function (event) {
        app.$data.history.onmk_li.p021 = event.target.getAttribute('n')
    })
    $('input[name="p022_li"]').click(function (event) {
        app.$data.history.onmk_li.p022 = event.target.getAttribute('n')
    })
    $('input[name="p023_li"]').click(function (event) {
        app.$data.history.onmk_li.p023 = event.target.getAttribute('n')
    })

}


function onk() {
    get_stad()
    get_onk_t()
    get_onk_n()
    get_onk_m()

    get_diag_code()
    get_diag_rslt()
}
function get_stad() {
    let kod = app.$data.history.dskz.kod

    let query = `
              query {
                N002(ds:"${kod}") {
                  kodSt
                }
              }`
    return fetch('graph_hospital/', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query })
    })
        .then(response => response.json())
        .then(data => {
            let stads = data.data.N002
            let stad = document.getElementById('stad-l')
            stad.innerText = ''
            stad.innerHTML = ''
            let str_stad = ''

            for (let s in stads) {
                let option = document.createElement("option")
                option.value = stads[s].kodSt
                stad.appendChild(option)
            }
        })
        .catch((e) => {
            // console.log(e)
        })


}
function get_onk_t() {
    let kod = app.$data.history.dskz.kod
    let query = `
              query {
                N003(ds:"${kod}") {
                  kodT
                }
              }`
    return fetch('graph_hospital/', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query })
    })
        .then(response => response.json())
        .then(data => {
            let onk_ts = data.data.N003
            let onk_t = document.getElementById('onk_t-l')
            onk_t.innerText = ''
            onk_t.innerHTML = ''
            for (let o in onk_ts) {
                let option = document.createElement("option")
                option.value = onk_ts[o].kodT
                onk_t.appendChild(option)
            }
        })
        .catch((e) => {
            // console.log(e)
        })
}
function get_onk_n() {
    let kod = app.$data.history.dskz.kod

    let query = `
              query {
                N004(ds:"${kod}") {
                  kodN
                }
              }`
    return fetch('graph_hospital/', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query })
    })
        .then(response => response.json())
        .then(data => {
            let onk_ns = data.data.N004
            let onk_n = document.getElementById('onk_n-l')
            onk_n.innerText = ''
            onk_n.innerHTML = ''
            for (let o in onk_ns) {
                let option = document.createElement("option")
                option.value = onk_ns[o].kodN
                onk_n.appendChild(option)
            }
        })
        .catch((e) => {
            // console.log(e)
        })


}
function get_onk_m() {
    let kod = app.$data.history.dskz.kod

    let query = `
              query {
                N005(ds:"${kod}") {
                  kodM
                }
              }`
    return fetch('graph_hospital/', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query })
    })
        .then(response => response.json())
        .then(data => {
            let onk_ms = data.data.N005
            let onk_m = document.getElementById('onk_m-l')
            onk_m.innerText = ''
            onk_m.innerHTML = ''
            for (let o in onk_ms) {
                let option = document.createElement("option")
                option.value = onk_ms[o].kodM
                onk_m.appendChild(option)
            }
        })
        .catch((e) => {
            // console.log(e)
        })
}
function get_diag_code() {
    let diag_code = app.$data.history.diag_tip
    var diag = document.getElementById("diag_code-l")
    let code = []
    diag.innerHTML = ''
    if (diag_code != undefined) {
        if (diag_code == 'Гистологический признак') {
            app.$data.sprav_list.N007.forEach(function (data) {
                code.push(data.mrfName)
            })


        }
        else {
            app.$data.sprav_list.N010.forEach(function (data) {
                code.push(data.kodIgh)
            })
        }
        for (let c in code) {
            let option = document.createElement("option")
            option.value = code[c]
            diag.appendChild(option)
        }
    }
}
function get_diag_rslt() {
    let diag_code = app.$data.history.diag_tip
    if (diag_code != NaN) {
        var diag = document.getElementById("diag_rslt-l")
        let code = []
        if (diag_code == 'Гистологический признак') {
            app.$data.sprav_list.N008.forEach(function (data) {
                code.push(data.rMName)
            })
        }
        else {
            app.$data.sprav_list.N011.forEach(function (data) {
                code.push(data.rIName)
            })
        }
        for (let c in code) {
            let option = document.createElement("option")
            option.value = code[c]
            diag.appendChild(option)
        }
    }
}



function Clear(event) {
    if (event.target.getAttribute("save") == 'true') {
        //Подумать нужно ли обновить запись у пользователя на раб.столе
        start_prot()
        if (app.$data.protoc == false) {
            save()
            app.default_temp()
            var med_card_menu = document.getElementById("med_card_menu")
            for (let menu of med_card_menu.querySelectorAll('a')) {
                menu.classList.remove("active")
            }
            $('#exampleModal').modal('hide')
        }
    }
    else {
        app.default_temp()
        var med_card_menu = document.getElementById("med_card_menu")
        for (let menu of med_card_menu.querySelectorAll('a')) {
            menu.classList.remove("active")
        }
        $('#exampleModal').modal('hide')
    }


}

function save() {
    let formData = new FormData()
    formData.append('history', JSON.stringify(app.$data.history))
    formData.append('type', 'save')

    var r = sendRequest('', 'post', formData)
        .then(response => {

        })
        .catch(error => {
        })
}

// change


$(function () {
    //Шапка
    $("#datp").change(function () {
        app.$data.history.datp = $("#datp").val()
    })

    $("#tm_otd").change(function () {
        app.$data.history.tm_otd = $("#tm_otd").val()
    })

    $("#datv").change(function () {
        app.$data.history.datv = $("#datv").val()
    })

    $("#datr").change(function () {
        app.$data.history.datr = $("#datr").val()
    })
    //

    //1.Персональные данные
    $("#otd").change(function () {
        onmk_disabled()
    })

    $("#npr_date").change(function () {
        app.$data.history.npr_date = $("#npr_date").val()
    })

    $("#adr_in").change(function () {
        app.$data.history.adr = $("#adr_in").val()
        app.$data.history.okatop = $("#adr_in").attr("data-kladr-id")
    })

    $("#vec").change(function () {
        app.$data.history.vec = $("#vec").val()

    })
    $("#m_roj_in").change(function () {
        app.$data.history.m_roj = $("#m_roj_in").val()
        app.$data.history.okatog = $("#m_roj_in").attr("data-kladr-id")
    })
    //2. Сведения о диагнозах
    $("#dskz_kod").change(function () {
        onmk_disabled()
    })
    $("#dat_otd").change(function () {
        app.$data.history.dat_otd = $("#dat_otd").val()
    })
    $("#tm_otd_d").change(function () {
        app.$data.history.tm_otd_d = $("#tm_otd_d").val()
    })
    $("#rslt").change(function () {
        onmk_disabled()
        post_mortem_disabled()
    })

    //
    $("#m_roj").change(function () {
        app.$data.history.m_roj = $("#m_roj").val()
    })
    $("#docdate").change(function () {
        app.$data.history.docdate = $("#docdate").val()
    })
    $("#ss").change(function () {
        app.$data.history.ss = $("#ss").val()
    })
    //
    $("#vb_a_datv").change(function () {
        app.$data.history.vb_a_datv = $("#vb_a_datv").val()
    })

    //
    $("#dat_l1").change(function () {
        app.$data.history.dat_l1 = $("#dat_l1").val()
    })
    $("#dat_l2").change(function () {
        app.$data.history.dat_l2 = $("#dat_l2").val()
    })


    //
    $("#mp_roj").change(function () {
        // console.log($("#mp_roj").attr("data-kladr-id"))
        app.$data.history.mp_roj = $("#mp_roj").val()
        app.$data.history.okatog_p = $("#mp_roj").attr("data-kladr-id")
        app.$data.history.okatop_p = $("#mp_roj").attr("data-kladr-id")
    })

    //
    $("#diag_date").change(function () {
        app.$data.history.diag_date = $("#diag_date").val()
    })
    $("#dt_cons").change(function () {
        app.$data.history.dt_cons = $("#dt_cons").val()
    })
    $("#d_prot").change(function () {
        app.$data.history.d_prot = $("#d_prot").val()
    })
    $("#naprdate").change(function () {
        app.$data.history.naprdate = $("#naprdate").val()
    })

})


var tabIsPressed = false;
var tabIsPressed_sh = false;

$(window).keydown(function (event) {
    if (event.keyCode == 17) {
        tabIsPressed = true; event.preventDefault();
    }
});

$(window).keydown(function (event) {
    if (event.keyCode == 16) {
        tabIsPressed_sh = true; event.preventDefault();
    }
});


$(window).keyup(function (event) {
    if (event.keyCode == 17) {
        tabIsPressed = false; event.preventDefault();
    }
});
$(window).keyup(function (event) {
    if (event.keyCode == 16) {
        tabIsPressed_sh = false; event.preventDefault();
    }
});


$(window).on('keydown', function (e) {
    if (tabIsPressed && event.keyCode === 67) {
        event.preventDefault();
        document.getElementById("btn_cancellation").click()
        return;
    }
});

$(window).on('keydown', function (e) {
    if (tabIsPressed && event.keyCode === 83) {
        event.preventDefault();
        document.getElementById("btn_save").click()
        return;
    }
});
// $(window).on('keydown', function (e) {
//     if (tabIsPressed && tabIsPressed_sh ) {
//         console.log('sd')
//     }
// });

// $(window).on('keydown', function (e) {
//     if (app.$data.inf_operation){
//         if (app.$data.history.oper.length > 1){
//             if (tabIsPressed && event.keyCode === 16) {
//                 let el = event.target
//                 let inp = $("#operation_table").find(`input[n="${ parseInt(el.getAttribute("n"),10) - 1}"][name="${el.getAttribute("name")}"]`)
//                 if (inp.length != 0){
//                     inp[0].focus()
//                 }
//             }
//         }
//     }
// });

$(window).on('keydown', function (e) {
    if (event.target.id == 'exampleModal') {
        // console.log(event.keyCode, event.key, event.code, event.charCode)
        var med_card_menu = document.getElementById("med_card_menu")
        for (let menu of med_card_menu.querySelectorAll('a')) {
            menu.classList.remove("active")
        }


        if (event.keyCode == 27) {
            if (app.$data.inf_pers_info) {
                menu_active(0, false)
            }
            else if (app.$data.inf_diagnoses) {
                menu_active(2, false)
            }
            else if (app.$data.inf_koyko) {
                menu_active(4, false)
                // Koyko_edit()
            }
            else if (app.$data.inf_operation) {
                menu_active(6, false)
            }
            else if (app.$data.inf_ks_zabolev) {
                // get_v_018_v_019()
                menu_active(8, false)
            }
            else if (app.$data.inf_complication) {
                menu_active(10, false)
            }
            else if (app.$data.inf_work_capacity) {
                menu_active(12, false)
            }
            else if (app.$data.inf_manipulation) {
                menu_active(14, false)
            }
            else if (app.$data.inf_translations) {
                menu_active(16, false)
            }
        }
        else if (event.keyCode == 96 || event.keyCode == 48) {
            console.log($("#fam").val())
            console.log(app.$data.history['fam'])
            $("#fam").focus()
            setTimeout(() => {
                app.$data.history['fam'] = app.$data.history['fam'].slice(0, -1)
            }, 1)

        }
        else if (event.keyCode === 112) {
            tab_f1()

        }

        else if (event.keyCode === 113) {
            if (app.$data.inf_pers_info) {
                menu_active(0, false)
                $("#otd").focus()
            }
            else if (app.$data.inf_diagnoses) {
                menu_active(2, false)
                $("#dsny_kod").focus()

            }
            else if (app.$data.inf_koyko) {
                menu_active(4, false)
                $('input[name="N"]').focus()
            }
            else if (app.$data.inf_operation) {
                menu_active(6, false)
                $('td[name="dato"] input').first().focus()
            }

            else if (app.$data.inf_ks_zabolev) {
                // get_v_018_v_019()
                menu_active(8, false)
                $("#ksg_osn").focus()
            }

            else if (app.$data.inf_complication) {
                menu_active(10, false)
                $('td[name="inf_oper"] select').first().focus()
            }

            else if (app.$data.inf_manipulation) {
                menu_active(14, false)
                $('td[name="datm"] input').first().focus()
            }
            else if (app.$data.inf_translations) {
                menu_active(16, false)
                $("#potd").focus()
            }
            else if (app.$data.inf_post_mortem) {
                menu_active(18, false)
                $("#wskr_date").focus()
            }
            else if (app.$data.inf_injury) {
                menu_active(20, false)
                $("#details_kod").focus()
            }
            else if (app.$data.inf_policy_passport_snills) {
                menu_active(22, false)
                $("#vds").focus()
            }
            else if (app.$data.inf_pregnancy) {
                menu_active(24, false)
                $("#vb_a_datv").focus()
            }
            else if (app.$data.inf_disability) {
                menu_active(26, false)
                $("#dat_l1").focus()
            }
            else if (app.$data.inf_patient_p) {
                menu_active(28, false)
                $("#fam_p").focus()
            }
            else if (app.$data.inf_onk) {
                menu_active(34, false)
                $("#ds1_t").focus()
            }
            else if (app.$data.inf_mo) {
                menu_active(36, false)
                $("#pmg").focus()
            }

        }

        else if (event.keyCode == 115) {
            if (app.$data.inf_operation) {
                Oper_add()
            }
            else if (app.$data.inf_complication) {
                Complication_add()
            }
            else if (app.$data.inf_manipulation) {
                manipulation_add()
            }
        }

        else if (event.keyCode === 49 || event.keyCode === 97) {
            menu_active(0, true)
            app.$data.inf_pers_info = true
        }
        else if (event.keyCode === 50 || event.keyCode === 98) {
            menu_active(2, true)
            app.$data.inf_diagnoses = true
        }
        else if (event.keyCode === 51 || event.keyCode === 99) {
            menu_active(4, true)
            app.$data.inf_koyko = true
            Koyko_edit()
        }
        else if (event.keyCode === 52 || event.keyCode === 100) {
            menu_active(6, true)
            app.$data.inf_operation = true
            Oper_edit()

        }
        else if (event.keyCode === 53 || event.keyCode === 101) {
            menu_active(8, true)
            app.$data.inf_ks_zabolev = true
            get_v_018_v_019()
        }
        else if (event.keyCode === 54 || event.keyCode === 102) {
            menu_active(10, true)
            app.$data.inf_complication = true
            Complication_edit()
        }
        else if (event.keyCode === 55 || event.keyCode === 103) {
            menu_active(12, true)
            app.$data.inf_work_capacity = true
            Select_trs()
        }
        else if (event.keyCode === 56 || event.keyCode === 104) {
            menu_active(14, true)
            app.$data.inf_manipulation = true
            Manipulation_edit()
        }
        else if (event.keyCode === 57 || event.keyCode === 105) {
            menu_active(16, true)
            app.$data.inf_translations = true
        }

        else if (event.keyCode === 65) {
            if (document.getElementById("list-profile-list_inf_post_mortem").classList.contains("disabled") == false) {
                menu_active(18, true)
                app.$data.inf_post_mortem = true
            }
        }
        else if (event.keyCode === 66) {
            menu_active(20, true)
            app.$data.inf_injury = true
        }
        else if (event.keyCode === 67) {
            menu_active(22, true)
            app.$data.inf_policy_passport_snills = true
        }
        else if (event.keyCode === 68) {
            if (document.getElementById("list-profile-list_inf_pregnancy").classList.contains("disabled") == false) {
                menu_active(24, true)
                app.$data.inf_pregnancy = true
            }
        }
        else if (event.keyCode === 69) {
            menu_active(26, true)
            app.$data.inf_disability = true
        }
        else if (event.keyCode === 70) {
            menu_active(28, true)
            app.$data.inf_patient_p = true
        }
        // else if (event.keyCode === 70){
        //     menu_active(28, true)
        //     app.$data.inf_patient_p = true
        // }
        else if (event.keyCode === 73) {
            if (document.getElementById("list-profile-list_inf_onmk").classList.contains("disabled") == false) {
                menu_active(32, true)
                app.$data.inf_onmk = true
                onmk()
            }
        }
        else if (event.keyCode === 74) {
            if (document.getElementById("list-profile-list_inf_onk").classList.contains("disabled") == false) {
                menu_active(34, true)
                app.$data.inf_onk = true
                onk()
            }
        }
        else if (event.keyCode === 75) {
            menu_active(36, true)
            app.$data.inf_mo = true
        }
        // else if (event.keyCode === 16){
        //     console.log('ВВерх')
        // }



    }
})

function tab_f1() {
    let tab = []
    tab.push(0)
    tab.push(2)
    if (document.getElementById("list-profile-list_inf_post_mortem").classList.contains("disabled") == false) {
        tab.push(18)
    }
    if (document.getElementById("list-profile-list_inf_pregnancy").classList.contains("disabled") == false) {
        tab.push(24)
    }
    if (document.getElementById("list-profile-list_inf_onmk").classList.contains("disabled") == false) {
        tab.push(32)
    }
    if (document.getElementById("list-profile-list_inf_onk").classList.contains("disabled") == false) {
        tab.push(34)
    }
    tab.push(4)
    tab.push(22)

    if (Next == null) {
        menu_active(2, true)
        app.$data.inf_diagnoses = true
        Next = 2
    }

    else {
        if (tab.indexOf(Next) != -1) {
            let step = tab.indexOf(Next) + 1
            Next = tab[step]

            if (Next == 18) {
                menu_active(18, true)
                app.$data.inf_post_mortem = true
            }
            else if (Next == 24) {
                menu_active(24, true)
                app.$data.inf_pregnancy = true
            }
            else if (Next == 32) {
                menu_active(32, true)
                app.$data.inf_onmk = true
            }
            else if (Next == 34) {
                menu_active(34, true)
                app.$data.inf_onk = true
            }
            else if (Next == 4) {
                menu_active(4, true)
                app.$data.inf_koyko = true
                Koyko_edit()
            }
            else if (Next == 22) {
                menu_active(22, true)
                app.$data.inf_policy_passport_snills = true
            }
            else {
                menu_active(0, true)
                app.$data.inf_pers_info = true
                Next = null
            }
        }
    }

}

function mod_adr() {
    app.$data.history.c_oksm = $("#c_oksm_in").val()
    app.$data.history.m_roj = $("#m_roj_in").val()
    app.$data.history.kv = $("#kv_in").val()
    app.$data.history.kp = $("#kp_in").val()
    app.$data.history.stro = $("#stro_in").val()
    app.$data.history.cj = $("#cj_in").val()
    app.$data.history.rai = $("#rai_in").val()
    // app.$data.history.okatog = $("#m_roj_in").attr("data-kladr-id")
}
function ksg_osn_onchange() {
    // console.log('ksg_osn_onchange')
    // console.log($("#ksg_osn").val())

    let query = `
          query{
              T006KsgCodeUslTitle(ksg:"${$("#ksg_osn").val()}"){
                ksg
                codeUsl
                title
              }
          }`
    fetch('graph_hospital/', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query })
    })
        .then(response => response.json())
        .then(data => {


            if (typeof (data.data.T006KsgCodeUslTitle[0]) != 'undefined') { app.$data.history.ksg_osn_all = data.data.T006KsgCodeUslTitle[0].ksg } else { app.$data.history.ksg_osn_all = '' }
            if (typeof (data.data.T006KsgCodeUslTitle[0]) != 'undefined') { app.$data.history.code_usl = data.data.T006KsgCodeUslTitle[0].codeUsl } else { app.$data.history.code_usl = '' }
            if (typeof (data.data.T006KsgCodeUslTitle[0]) != 'undefined') { app.$data.history.code_usl_name = data.data.T006KsgCodeUslTitle[0].title } else { app.$data.history.code_usl_name = '' }

            let query = `
                  query{
                      groupKcDkk(ksg:"${data.data.T006KsgCodeUslTitle[0].ksg}"){
                        kod
                      }
                  }`
            fetch('graph_hospital/', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query })
            })
                .then(response => response.json())
                .then(data => {
                    if (typeof (data.data.groupKcDkk[0]) != 'undefined') { app.$data.history.oopkk = data.data.groupKcDkk[0].kod } else { app.$data.history.oopkk = '' }

                })
                .catch((e) => {
                    // console.log(e)
                })
        })
        .catch((e) => {
            // console.log(e)
        })

}
function get_v_018_v_019() {
    if (app.$data.history.vds == 'ВТМП баз.программа ОМС') {
        let query = `
          query {
            V018Bpoms{
                idhvid
               }
            V019Bpoms{
                hvid
              }
          }`
        return fetch('graph_hospital/', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query })
        })
            .then(response => response.json())
            .then(data => {
                let vme = data.data.V019Bpoms
                if (vme != null) {
                    for (v in vme) {
                        let op = document.createElement("option")
                        op.innerHTML = vme[v].hvid
                        document.getElementById("vid_vme_l").appendChild(op)
                    }
                }

                let hmp = data.data.V018Bpoms
                if (hmp != null) {
                    for (h in hmp) {
                        let op = document.createElement("option")
                        op.innerHTML = hmp[h].idhvid
                        document.getElementById("vid_hmp_l").appendChild(op)
                    }
                }

            })
            .catch((e) => {
                // console.log(e)
            })
    }
    else if (app.$data.history.vds == 'ВТМП сверхбаз.программа') {
        let query = `
          query {
            V019Sboms{
            idhvid
            }
          }`
        fetch('graph_hospital/', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query })
        })
            .then(response => response.json())
            .then(data => {
                let vme = data.data.V019Sboms
                if (vme != null) {
                    for (v in vme) {
                        let op = document.createElement("option")
                        op.innerHTML = vme[v].idhvid
                        document.getElementById("vid_vme_l").appendChild(op)
                    }
                }
            })
            .catch((e) => {
                // console.log(e)
            })
    }
}

function code_usl() {
    var query = ''
    if (app.$data.history.vds == 'ВТМП баз.программа ОМС') {
        if ($("#metod_hmp").val() != '' && $("#vid_hmp").val() != '') {
            query = `
              query {
                 TarVt(isf:"Д",kodStat:"${$("#metod_hmp").val()}",metod:"${$("#vid_hmp").val()}"){
                    kod
                    naim
                    }
              }`
        }

    }
    else {
        if ($("#metod_hmp").val() != '' && $("#vid_hmp").val() != '') {
            query = `
              query {
                TarVt(isf:"5",kodStat:"${$("#metod_hmp").val()}",metod:"${$("#vid_hmp").val()}"){
                    kod
                    naim
                   }
              }`
        }
    }
    if (query != '') {
        fetch('graph_hospital/', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query })
        })
            .then(response => response.json())
            .then(data => {
                // console.log(data.data.TarVt)
                // console.log(data.data.TarVt.length)
                if (data.data.TarVt.length > 0) {
                    app.$data.history.code_usl_vt = data.data.TarVt[0].kod
                    app.$data.history.code_usl_vt_name = data.data.TarVt[0].naim
                }
                else {
                    app.$data.history.code_usl_vt = ''
                    app.$data.history.code_usl_vt_name = ''
                }
            })
            .catch((e) => {
                // console.log(e)
            })
    }

}


function change_dat_pe() {
    app.$data.history.dat_pe = $("#dat_pe").val()
}

function change_wskr_date() {
    app.$data.history.wskr_date = $("#wskr_date").val()
}

function change_tm_let() {
    app.$data.history.tm_let = $("#tm_let").val()
}



function menu_active(n, b) {
    if (b) {
        app.default_temp()

    }
    med_card_menu.childNodes[n].classList.add("active")
}

function fff() {
    // console.log('asaaa');
    // fetch('graph_hospital/', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({
    //         query: `
    //         {
    //              DsList(ds:"A00") {
    //                 kod
    //  }
    //         }
    //         `
    //     })
    //
    // })

    const query = `
          query {
            DsList(ds:"A00") {
              kod
            }
          }`
    return fetch('graph_hospital/', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query })
    })
        .then(response => response.json())
        .then(data => {
            // console.log(data.data.DsList)
            return data
        })
        .catch((e) => {
            // console.log(e)
        })

}

$(window).on('keydown', function (e) {
    if (event.target.id != 'exampleModal') {
        console.log(event.keyCode, event.key, event.code, event.charCode)
        if (event.keyCode === 113) {
            $("#inp_search_history").focus()
        }
        else if (tabIsPressed_sh) {
            if (app.$data.inf_operation) {
                if (app.$data.history.oper.length > 1) {
                    let el = event.target
                    let inp = $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10) - 1}"][name="${el.getAttribute("name")}"]`)
                    if (inp.length != 0) {
                        inp[0].focus()
                    }
                    else{
                        let inp = $("#operation_table").find(`select[n="${parseInt(el.getAttribute("n"), 10) - 1}"][name="${el.getAttribute("name")}"]`)
                        if (inp.length != 0) {
                            inp[0].focus()
                        }
                    }
                }
            }
            else if (app.$data.inf_complication) {
                if (app.$data.history.oslo.length > 1) {
                    let el = event.target
                    // console.log(el)
                    let inp = $("#complication_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10) - 1}"][name="${el.getAttribute("name")}"]`)
                    if (inp.length != 0) {
                        inp[0].focus()
                    }
                    else{
                        let inp = $("#complication_table").find(`select[tr="${parseInt(el.getAttribute("tr"), 10) - 1}"][name="${el.getAttribute("name")}"]`)
                        if (inp.length != 0) {
                            inp[0].focus()
                        }
                    }
                }
            }
            else if (app.$data.inf_manipulation) {
                if (app.$data.history.manipulation.length > 1) {
                    let el = event.target
                    let inp = $("#manipulation_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10) - 1}"][name="${el.getAttribute("name")}"]`)
                    if (inp.length != 0) {
                        inp[0].focus()
                    }
                    else{
                        let inp = $("#manipulation_table").find(`select[tr="${parseInt(el.getAttribute("tr"), 10) - 1}"][name="${el.getAttribute("name")}"]`)
                        if (inp.length != 0) {
                            inp[0].focus()
                        }
                    }
                }
            }
            
        }
        else if (event.key === 'Control') {
            if (app.$data.inf_operation) {
                if (app.$data.history.oper.length > 1) {
                    let el = event.target
                    let inp = $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10) + 1}"][name="${el.getAttribute("name")}"]`)
                    if (inp.length != 0) {
                        inp[0].focus()
                    }
                    else{
                        let inp = $("#operation_table").find(`select[n="${parseInt(el.getAttribute("n"), 10) + 1}"][name="${el.getAttribute("name")}"]`)
                        if (inp.length != 0) {
                            inp[0].focus()
                        }
                    }
                }

            }
            else if (app.$data.inf_complication) {
                if (app.$data.history.oslo.length > 1) {
                    let el = event.target
                    // console.log(el)
                    let inp = $("#complication_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10) + 1}"][name="${el.getAttribute("name")}"]`)
                    if (inp.length != 0) {
                        inp[0].focus()
                    }
                    else{
                        let inp = $("#complication_table").find(`select[tr="${parseInt(el.getAttribute("tr"), 10) + 1}"][name="${el.getAttribute("name")}"]`)
                        if (inp.length != 0) {
                            inp[0].focus()
                        }
                    }
                }
            }
            else if (app.$data.inf_manipulation) {
                if (app.$data.history.manipulation.length > 1) {
                    let el = event.target
                    let inp = $("#manipulation_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10) + 1}"][name="${el.getAttribute("name")}"]`)
                    if (inp.length != 0) {
                        inp[0].focus()
                    }
                    else{
                        let inp = $("#manipulation_table").find(`select[tr="${parseInt(el.getAttribute("tr"), 10) + 1}"][name="${el.getAttribute("name")}"]`)
                        if (inp.length != 0) {
                            inp[0].focus()
                        }
                    }
                }
            }
        }
    }
})

function onch(){

    

//     // tab_f1()
//     // console.log(event.target.id)
// if (event.target.getAttribute("id") == 'p_per'){
//     document.getElementById("list-profile-list_inf_diagnoses").click()
//     // document.getElementById("list-home-list_inf_pers_info").classList.remove("active")
//     // document.getElementById("dsny_kod").focus()
//     // // console.log(event.target.id)
//     // // document.getElementById("list-home-list_inf_pers_info").click()
//     // // // console.log(event.target.id)
//     // $("#dsny_kod").focus()

// }


// else if (event.target.getAttribute("id") == 'rslt'){
//     document.getElementById("list-profile-list_inf_diagnoses").classList.remove("active")

// }
// else if (event.target.getAttribute("id") == 'otd_y'){
//     document.getElementById("list-profile-list_inf_post_mortem").classList.remove("active")
// }
// else if (event.target.getAttribute("id") == 'm_prer'){
//     document.getElementById("list-profile-list_inf_pregnancy").classList.remove("active")
// }

// else if (event.target.getAttribute("id") == 'ss'){
//     document.getElementById("list-profile-list_inf_policy_passport_snills").classList.remove("active")
// }
// else if (event.target.getAttribute("id") == 'list-profile-list_inf_onk'){
//     document.getElementById("list-profile-list_inf_policy_passport_snills").classList.remove("active")
// }
// document.getElementById("modal-content").click()
}