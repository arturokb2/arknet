
var app = new Vue({
    el: '#app_hospital',
    data: {
        list_ds: Array(),
        sprav_list: [],
        // Поиск записей истории
        check_history: true,
        search_history: '',
        check_response_history: false,
        response_history: [],
        //Получаем данные из истории
        history: [],

        protoc: false,
        // Побочные поля
        ASCII: {
            "й": "Q", "ц": "W", "у": "E", "к": "R", "е": "T",
            "н": "Y", "г": "U", "ш": "I", "щ": "O",
            "з": "P", "ф": "A", "ы": "S", "в": "D", "а": "F",
            "п": "G", "р": "H", "о": "J", "л": "K", "д": "L",
            "я": "Z", "ч": "X", "с": "C", "м": "V", "и": "B",
            "т": "N", "ь": "M",
            "Й": "Q", "Ц": "W", "У": "E", "К": "R", "Е": "T",
            "Н": "Y", "Г": "U", "Ш": "I", "Щ": "O",
            "З": "P", "Ф": "A", "Ы": "S", "В": "D", "А": "F",
            "П": "G", "Р": "H", "О": "J", "Л": "K", "Д": "L",
            "Я": "Z", "Ч": "X", "С": "C", "М": "V", "И": "B",
            "Т": "N", "Ь": "M"
        },
        ds_naim: '',

        inf_onmk_sp: false,
        inf_onmk_li: false,
        next: [],
        history_rest: Object(),


    },
    mounted: function () {
        this.get_sprav_list()
    },
    methods: {
        get_sprav_list: function () {
            let query = `
          query{
              V005{
                id,
                polname
              },
              Otde{
                id,
                naim
              },
              RabNer{
                id,
                naim
              },
              T004{
                id,
                name
              },
              F003{
                id,
                naim
              },
              V014{
                id,
                tipName
              },
              Prpg{
                id,
                naim
              },
              Vrzb{
                id,
                naim
              },
              PER{
                id,
                naim
              },
              V012{
                id,  
                idIz,
                izName
               },
              V009{
                id,
                idTip,
                tipName
               },
              V020{
                id,
                kPrname
              },
              Vra{
                id,
                kod
              },
              PROsob{
                  id,
                  kod,
                  naim
              },
              V001{
                 id,
                 kod
              },
              anesthesia{
                id,  
                kod
              },
              T006{
                id,  
                codeUslKz
              },
              Pope{
                id,  
                kod
              },
              AbObsh{
                id,  
                kod
              },
              PRPer{
                id,
                naim
              },
              Prli{
                id,  
                kod
              },
              Trv{
                 id,
                 naim
              },
              Trvnas{
                 id, 
                 naim
              },
              Isfin{
                 id, 
                 naim
              },
              Skom{
                 id, 
                 naim
              },
              F008{
                id,  
                tipName
              },
              F011{
                id,  
                docname
              },
              TipPb{
                id,  
                naim
              },
              MetPb{
                id,  
                naim
               },
              Oksm{
                id,  
                naim
               },
               N007{
                id,   
                mrfName
               },
               N010{
                id,   
                kodIgh
               },
               N008{
                id,   
                rMName
               },
               N011{
                id,   
                rIName
               },
               N018{
                id,   
                reasName
               },
               V027{
                id,   
                nCz
               },
               N019{
                id,   
                consName
               },
               N013{
                id,   
                tlechName
               },
               N014{
                id,   
                thirName
               },
               N001{
                id,   
                protName
               },
               V028{
                id,   
                nVn
               },
               V029{
                id,   
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
            let search_history_url = 'http://' + window.location.host + '/hospital/api/search_history/'
            if (this.search_history != '') {
                let url = search_history_url + '?nib=' + this.search_history
                // var formData = new FormData()
                // formData.append('history', this.search_history)
                // formData.append('type', 'search')
                var r = sendRequest(url, 'get')
                    .then(response => {
                        this.check_response_history = true
                        this.response_history = response.data

                        setTimeout(() => {
                            $("#all_nhistory button").first().focus()
                        }, 500)

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
            fetch('http://' + window.location.host + '/hospital/api/history/' + id, {
                method: 'get',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
                .then(response => response.json())
                .then(data => {
                    this.history_rest = data
                    console.log(this.history_rest)
                    console.log(this.history_rest['patient'][0])
                    this.history_rest.datp = moment(this.history_rest.datp).format('DD-MM-YYYY')
                    this.history_rest.datv = moment(this.history_rest.datv).format('DD-MM-YYYY')
                    this.history_rest['patient'][0].datr = moment(this.history_rest['patient'][0].datr).format('DD-MM-YYYY')
                    // moment().format('YYYY-MM-DD')
                })
                .catch((e) => {
                })


            // var rest = sendRequest('http://'+window.location.host+'/hospital/api/history/'+id, 'get')
            // .then(resp => {
            //     app.$data.history_rest = resp.data
            // })
            // .catch(error => {
            // })

            //     console.log(app.$data.history_rest)


            var formData = new FormData()
            formData.append('id', id)
            formData.append('type', 'data_history')
            var r = sendRequest('', 'post', formData)
                .then(response => {

                    // var rest = sendRequest('http://'+window.location.host+'/hospital/api/history/'+id, 'get')
                    // .then(resp => {
                    //     app.$data.history_rest = resp.data
                    // })
                    // .catch(error => {
                    // })

                    //     console.log(app.$data.history_rest)

                    this.history = response.data.rez



                    if (response.data.rez.dskz.kod[0] == 'O') {
                        document.getElementById("list-profile-list_inf_pregnancy").classList.remove("disabled")
                    }
                    else {
                        document.getElementById("list-profile-list_inf_pregnancy").classList.add("disabled")
                    }


                    var otd = this.history.otd
                    var dskz = this.history.dskz.kod
                    var res = $('#rslt').val()
                    var otde = ['НЕВРОЛОГИЯ N1', 'НЕВРОЛОГИЯ N2', 'НЕВРОЛОГИЯ N3']
                    var resl = ['Умер 105', 'Умер в приёмном покое 106']
                    var ds = ['G45', 'G46', 'I60', 'I60.0', 'I60.1', 'I60.2', 'I60.3', 'I60.4', 'I60.5',
                        'I60.6', 'I60.7', 'I60.8', 'I60.9', 'I61', 'I61.0', 'I61.1', 'I61.2', 'I61.3',
                        'I61.4', 'I61.5', 'I61.6', 'I61.8', 'I61.9', 'I62', 'I62.0', 'I62.1', 'I62.9',
                        'I63', 'I63.0', 'I63.1', 'I63.2', 'I63.3', 'I63.4', 'I63.5', 'I63.6', 'I63.8', 'I63.9']


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
                    // console.log(data)
                    if (id == 'dsny_kod') {
                        this.history.dsny.naim = data.data.DsName[0].naim.substr(0, 50)
                    }
                    else if (id == 'ds_0_kod') {
                        this.history.ds_0.naim = data.data.DsName[0].naim.substr(0, 50)
                    }
                    else if (id == 'dsk_kod') {
                        this.history.dsk.naim = data.data.DsName[0].naim.substr(0, 50)
                    }
                    else if (id == 'dskz_kod') {
                        this.history.dskz.naim = data.data.DsName[0].naim.substr(0, 50)
                    }
                    else if (id == 'ds_osl_kod') {
                        this.history.ds_osl.naim = data.data.DsName[0].naim.substr(0, 50)
                    }
                    else if (id == 'dsc_kod') {
                        this.history.dsc.naim = data.data.DsName[0].naim.substr(0, 50)
                    }
                    else if (id == 'dson_kod') {
                        this.history.dson.naim = data.data.DsName[0].naim.substr(0, 50)
                    }
                    else if (id == 'ds_let_kod') {
                        this.history.ds_let.naim = data.data.DsName[0].naim.substr(0, 50)
                    }
                    else if (id == 'dspat_kod') {
                        this.history.dspat.naim = data.data.DsName[0].naim.substr(0, 50)
                    }
                    else if (id == 'details_kod') {
                        this.history.details.naim = data.data.DsName[0].naim.substr(0, 50)
                    }

                })
                .catch((e) => {
                    // console.log(e)
                })
        },
        next_inf_pers_info: function () {
            document.getElementById("list-home-list_inf_pers_info").click()
            setTimeout(() => {
                $("#fam").focus()
            }, 1000)
        },
        next_inf_diagnoses: function () {
            document.getElementById("list-profile-list_inf_diagnoses").click()

            setTimeout(() => {
                $("#dsny_kod").focus()
            }, 500)
        },
        next_inf_koyko: function () {
            document.getElementById("list-profile-list_inf_koyko").click()
        },
        next_inf_operation: function () {
            document.getElementById("list-profile-list_inf_operation").click()
        },
        next_inf_ks_zabolev: function () {
            document.getElementById("list-profile-list_inf_ks_zabolev").click()
            if (app.history.vds != 'ВТМП баз.программа ОМС' && app.history.vds != 'ВТМП сверхбаз.программа') {
                setTimeout(() => {
                    $("#ksg_osn").focus()
                    this.ksg_osn_onchange()
                }, 500)
            }
            else {
                setTimeout(() => {
                    $("#metod_hmp").focus()
                }, 500)
            }
        },
        next_inf_manipulation: function () {
            setTimeout(() => {
                document.getElementById("list-profile-list_inf_manipulation").click()
            }, 500)
        },
        next_inf_translations: function () {
            setTimeout(() => {
                $("#potd").focus()
            }, 800)
        },
        next_inf_post_mortem: function () {
            setTimeout(() => {
                $("#wskr_date").focus()
            }, 500)
        },
        next_inf_injury: function () {
            setTimeout(() => {
                $(".dskz_kod").focus()
            }, 500)
        },
        next_inf_policy_passport_snills: function () {
            setTimeout(() => {
                $("#vds").focus()
            }, 500)
        },
        next_inf_pregnancy: function () {
            setTimeout(() => {
                $("#vb_a_datv").focus()
            }, 500)
        },
        next_inf_disability: function () {
            setTimeout(() => {
                $("#dat_l1").focus()
            }, 500)
        },
        next_inf_patient_p: function () {
            setTimeout(() => {
                $("#fam_p").focus()
            }, 500)
        },
        next_inf_adr: function () {
            setTimeout(() => {
                $("#c_oksm_in").focus()
            }, 500)
        },
        next_inf_onk: function () {
            setTimeout(() => {
                $("#ds1_t").focus()
            }, 500)
        },
        next_inf_mo: function () {
            setTimeout(() => {
                $("#pmg").focus()
            }, 500)
        },
        ksg_osn_onchange: function () {
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

        },
        code_usl: function () {
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

        },
        get_v_018_v_019: function () {
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
        },
        Select_trs: function () {
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
                        document.getElementById("list-profile-list_inf_work_capacity").click()
                    }


                    if (trs_radio[trs].textContent.replace(/\s+/g, ' ').trim() == v_trs) {
                        trs_radio[trs].childNodes[0].checked = true
                    }
                }
                catch (err) {
                }
            }
        },
        onmk: function () {
            this.Onmk_sp_u()
            this.Onmk_li_u()
        },
        Onmk_sp_u: function () {
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
        },
        Onmk_li_u: function () {

        },
        onk: function () {
            this.get_stad()
            this.get_onk_t()
            this.get_onk_n()
            this.get_onk_m()
            this.get_diag_code()
            this.get_diag_rslt()
        },
        get_stad: function () {
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


        },
        get_onk_t: function () {
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
        },
        get_onk_n: function () {
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


        },
        get_onk_m: function () {
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
        },
        get_diag_code: function () {
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
        },
        get_diag_rslt: function () {
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
        },
        onmk_disabled: function () {
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
        },
        next_tabs: function () {
            el = event.target
            if (el.id == "rslt") {
                if (app.$data.history.dskz.kod[0] == "O") {
                    document.getElementById("list-profile-list_inf_pregnancy").click()
                }
                else if (app.$data.history.dskz.kod[0] == "C") {
                    document.getElementById("list-profile-list_inf_onk").click()
                }
                else if ((app.$data.history.rslt == "Умер 105") || (app.$data.history.rslt == "Умер в приёмном покое 106")) {
                    document.getElementById("list-profile-list_inf_post_mortem").click()
                }
                else if ((app.$data.history.rslt == "Переведён в др. ЛПУ 102") || (app.$data.history.rslt == "Переведён в дневной стационар 103")
                    || (app.$data.history.rslt == "Переведён на другой профиль коек 104")) {
                    document.getElementById("list-profile-list_inf_translations").click()
                }

                else {
                    document.getElementById("list-profile-list_inf_koyko").click()
                }
            }
            if (el.id == "m_prer") {
                if ((app.$data.history.rslt == "Умер 105") || (app.$data.history.rslt == "Умер в приёмном покое 106")) {
                    document.getElementById("list-profile-list_inf_post_mortem").click()
                }
                else {
                    document.getElementById("list-profile-list_inf_koyko").click()
                }
            }
            if (el.id == "otd_y") {
                if (document.getElementById("list-profile-list_inf_onmk").classList.contains("disabled")) {
                    document.getElementById("list-profile-list_inf_koyko").click()
                }
                else {
                    document.getElementById("list-profile-list_inf_onmk").click()
                }
            }
            if (el.id == "napr_usl") {
                document.getElementById("list-profile-list_inf_koyko").click()
            }
        },
        adr_in: function () {
            // this.history.adr = $("#adr_in").val()
            // this.history.okatop = $("#adr_in").attr("data-kladr-id")
            // console.log(this.history.adr,this.history.okatop)
        },
        replace_code_usl: function () {
            let code = document.getElementById("ksg_osn")
            code.value = code.value.replace(",", ".")
        },
        replace_ksg_sop: function () {
            let sop = document.getElementById("ksg_sop")
            sop.value = sop.value.replace(",", ".")
        },
        save: function () {
            // patient
            let patient = this.history_rest.patient[0]
            let patient_datr = patient.datr.split('-')


            fetch('http://' + window.location.host + '/hospital/api/patient_update/' + app.$data.history_rest.patient[0].id + '/', {
                method: 'put',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "fam": patient.fam,
                    "im": patient.im,
                    "ot": patient.ot,
                    "pol": patient.pol.id,
                    "datr": patient_datr[2] + '-' + patient_datr[1] + '-' + patient_datr[0]
                }),
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                })
                .catch((e) => {
                })
            //Sluchay
            let sluchay_datp = this.history_rest.datp.split('-')
            let sluchay_datv = this.history_rest.datv.split('-')
            console.log(this.history_rest.tm_otd)

            fetch('http://' + window.location.host + '/hospital/api/sluchay_update/' + app.$data.history_rest.id + '/', {
                method: 'put',
                headers: {
                    'Content-Type': 'application/json',
                },

                body: JSON.stringify({
                    "datp": sluchay_datp[2]+'21' + '-' + sluchay_datp[1] + '-' + sluchay_datp[0],
                    "tm_otd": this.history_rest.tm_otd,
                    "datv": sluchay_datv[2]+'21' + '-' + sluchay_datv[1] + '-' + sluchay_datv[0],

                }),
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                })
                .catch((e) => {
                })



            // let otd = document.getElementById("otd")
            // console.log(otd)
            // let formData = new FormData()
            // formData.append('history', JSON.stringify(app.$data.history))
            // formData.append('type', 'save')

            // var r = sendRequest('', 'post', formData)
            //     .then(response => {

            //     })
            //     .catch(error => {
            //     })
            // setTimeout(() => {
            //     let an_rem = document.getElementById("an_rem")
            //     an_rem.setAttribute("style", "display:none")
            //     document.getElementById("inp_search_history").focus()
            // }, 500)
        },
        update_pol: function () {
            let pol = $("#mcp-pol-l").find(`option[value="${this.history_rest['patient'][0]['pol'].polname}"]`).first()
            this.history_rest['patient'][0]['pol'].id = pol[0].getAttribute('n_id')
            this.history_rest['patient'][0]['pol'].polname = pol[0].value
        }

    }
})

function Get_data_cards() {
    let id = this.event.target.getAttribute("id")
    app.get_data_cards(id)
    app.next_inf_pers_info()
    mask()
    key()

}


function key() {
    $(window).on('keydown', function (e) {
        // console.log(event)
        // console.log(event.target.id, event.keyCode)
        // console.log(app.$data.history)
        // if (event.target.id == "datp"){
        //     if (event.keyCode == 13){
        //         $("tm_otd").focus()
        //         console.log('qwe13')

        //     }
        // }
        next_tab()
        let inf_operation = document.getElementById("inf_operation")
        if (inf_operation.classList.contains('active')) {
            let operation_table = document.getElementById("operation_table")
            if (operation_table) {
                if (event.keyCode == 45) {
                    document.getElementById("add_tr_operation").click()
                    $('input[name="dato"]').last().focus()
                }
                if (event.keyCode == 46) {
                    if (app.$data.history.oper.length != 0) {
                        Oper_delete($(`tr[n="${event.target.getAttribute("n")}"]`)[0].childNodes[0])
                        $('td[name="dato"] input').last().focus()
                    }

                }
            }
        }
        let inf_complication = document.getElementById("inf_complication")
        if (inf_complication.classList.contains('active')) {
            let complication_table = document.getElementById("complication_table")
            if (complication_table) {
                if (event.keyCode == 45) {
                    // Complication_add()
                    document.getElementById("add_tr_complication").click()
                    $('select[name="inf_oper"]').last().focus()
                }
                if (event.keyCode == 46) {
                    if (app.$data.history.oslo.length != 0) {
                        Complication_delete($(`tr[n="${event.target.getAttribute("tr")}"]`)[0].childNodes[0])
                        $('select[name="inf_oper"]').last().focus()
                    }
                }
            }
        }
        let inf_manipulation = document.getElementById("inf_manipulation")
        if (inf_manipulation.classList.contains('active')) {
            let manipulation_table = document.getElementById("manipulation_table")
            if (manipulation_table) {
                if (event.keyCode == 45) {
                    document.getElementById("add_tr_manipulation").click()
                    $('input[name="datm"]').last().focus()
                }
                if (event.keyCode == 46) {
                    if (app.$data.history.manipulation.length != 0) {
                        Manipulation_delete($(`tr[n="${event.target.getAttribute("tr")}"]`)[0].childNodes[0])
                        $('input[name="datm"]').last().focus()
                    }
                }
            }
        }

        if (event.keyCode == 36) {
            document.getElementById("save").click()
        }
        if (event.keyCode == 35) {
            document.getElementById("save").click()
            // document.getElementById("сancel").click()
        }

        if (document.getElementById("list-home-list_inf_pers_info").classList.contains('active')) {

            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-home-list_inf_pers_info")) {
                next_tab()
            }

            if (event.keyCode == 19) {
                let header_left = $(".header-left").find('input[type=text]')
                let header_right = $(".header-right").find('input[type=text]')
                for (left of header_left) {
                    left.blur()
                }
                for (right of header_right) {
                    right.blur()
                }
                let pers = $("#inf_pers_info").find('input[type=text]')
                for (p of pers) {
                    p.blur()
                }



            }

            if (event.target.id == "fam") {
                if (event.keyCode == 13) {
                    $("#im").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.fam = ""
                }
            }
            else if (event.target.id == "im") {
                if (event.keyCode == 13) {
                    $("#ot").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.im = ""
                }
                if (event.keyCode == 33) {
                    $("#fam").focus()
                }
            }
            else if (event.target.id == "ot") {
                if (event.keyCode == 13) {
                    $("#pol").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.ot = ""
                }
                if (event.keyCode == 33) {
                    $("#im").focus()
                }
            }

            else if (event.target.id == "pol") {
                if (event.keyCode == 13) {
                    $("#datp").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.pol = ""
                }
                if (event.keyCode == 33) {
                    $("#ot").focus()
                }
            }

            else if (event.target.id == "datp") {
                if (event.keyCode == 13) {
                    $("#tm_otd").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.datp = ""
                }
                if (event.keyCode == 33) {
                    $("#pol").focus()
                }
            }

            else if (event.target.id == "tm_otd") {
                if (event.keyCode == 13) {
                    // console.log(document.getElementById("otd-l").getAttribute())
                    $("#datv").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.tm_otd = ""
                }
                if (event.keyCode == 33) {
                    $("#datp").focus()
                }
            }

            else if (event.target.id == "datv") {
                if (event.keyCode == 13) {
                    $("#datr").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.datv = ""
                }
                if (event.keyCode == 33) {
                    $("#tm_otd").focus()
                }
            }

            else if (event.target.id == "datr") {
                if (event.keyCode == 13) {
                    $("#otd").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.datr = ""
                }
                if (event.keyCode == 33) {
                    $("#datv").focus()
                }
            }

            else if (event.target.id == "otd") {
                if (event.keyCode == 13) {
                    $("#vec").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.otd = ""
                }
                if (event.keyCode == 33) {
                    $("#datr").focus()
                }
            }

            else if (event.target.id == "vec") {
                if (event.keyCode == 13) {
                    // $("#m_roj_1").focus()
                    document.getElementById("list-profile-list_inf_adr").click()
                }
                if (event.keyCode == 33) {
                    $("#otd").focus()
                }
            }

            else if (event.target.id == "m_roj_1") {
                if (event.keyCode == 33) {
                    $("#vec").focus()
                }
            }

            else if (event.target.id == "adr_in") {
                if (event.keyCode == 13) {
                    $("#rab").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.adr_in = ""
                    document.getElementById("adr_in").value = ""
                }
                if (event.keyCode == 33) {
                    $("#m_roj_1").focus()
                }
            }

            else if (event.target.id == "rab") {
                if (event.keyCode == 13) {
                    $("#prof").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.rab = ""
                }
                if (event.keyCode == 33) {
                    $("#adr_in").focus()
                }
            }

            else if (event.target.id == "prof") {
                if (event.keyCode == 13) {
                    $("#r_n").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.prof = ""
                }
                if (event.keyCode == 33) {
                    $("#rab").focus()
                }
            }

            else if (event.target.id == "r_n") {
                if (event.keyCode == 13) {
                    $("#in_t").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.r_n = ""
                }
                if (event.keyCode == 33) {
                    $("#prof").focus()
                }
            }

            else if (event.target.id == "in_t") {
                if (event.keyCode == 13) {
                    $("#lpy").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.in_t = ""
                }
                if (event.keyCode == 33) {
                    $("#r_n").focus()
                }
            }

            else if (event.target.id == "lpy") {
                if (event.keyCode == 13) {
                    $("#npr_num").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.lpy = ""
                }
                if (event.keyCode == 33) {
                    $("#in_t").focus()
                }
            }

            else if (event.target.id == "npr_num") {
                if (event.keyCode == 13) {
                    $("#npr_date").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.npr_num = ""
                }
                if (event.keyCode == 33) {
                    $("#lpy").focus()
                }
            }

            else if (event.target.id == "npr_date") {
                if (event.keyCode == 13) {
                    $("#alg").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.npr_date = ""
                }
                if (event.keyCode == 33) {
                    $("#npr_num").focus()
                }
            }

            else if (event.target.id == "alg") {
                if (event.keyCode == 13) {
                    $("#goc").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.alg = ""
                }
                if (event.keyCode == 33) {
                    $("#npr_date").focus()
                }
            }

            else if (event.target.id == "goc") {
                if (event.keyCode == 13) {
                    $("#prpg").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.goc = ""
                }
                if (event.keyCode == 33) {
                    $("#alg").focus()
                }
            }

            else if (event.target.id == "prpg") {
                if (event.keyCode == 13) {
                    $("#vrez").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.prpg = ""
                }
                if (event.keyCode == 33) {
                    $("#goc").focus()
                }
            }

            else if (event.target.id == "vrez") {
                if (event.keyCode == 13) {
                    $("#p_per").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.vrez = ""
                }
                if (event.keyCode == 33) {
                    $("#prpg").focus()
                }
            }

            else if (event.target.id == "p_per") {
                if (event.keyCode == 13) {
                    app.next_inf_diagnoses()
                }
                if (event.keyCode == 46) {
                    app.$data.history.p_per = ""
                }
                if (event.keyCode == 33) {
                    $("#vrez").focus()
                }
            }

        }

        if (document.getElementById("list-profile-list_inf_diagnoses").classList.contains('active')) {
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_diagnoses")) {
                next_tab()
            }
            if (event.keyCode == 19) {
                let diagnoses = $("#inf_diagnoses").find('input[type=text]')
                for (d of diagnoses) {
                    d.blur()
                }
            }


            if (event.target.id == "dsny_kod") {
                if (event.keyCode == 13) {
                    $("#ds_0_kod").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.dsny.kod = ""
                    app.$data.history.dsny.naim = ""

                }
            }
            else if (event.target.id == "ds_0_kod") {
                if (event.keyCode == 13) {
                    $("#dsk_kod").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.ds_0.kod = ""
                    app.$data.history.ds_0.naim = ""
                }
                if (event.keyCode == 33) {
                    $("#dsny_kod").focus()
                }
            }

            else if (event.target.id == "dsk_kod") {
                if (event.keyCode == 13) {
                    $("#dskz_kod").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.dsk.kod = ""
                    app.$data.history.dsk.naim = ""

                }
                if (event.keyCode == 33) {
                    $("#ds_0_kod").focus()
                }
            }

            else if (event.target.id == "dskz_kod") {
                if (event.keyCode == 13) {
                    $("#ds_osl_kod").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.dskz.kod = ""
                    app.$data.history.dskz.naim = ""
                }
                if (event.keyCode == 33) {
                    $("#dsk_kod").focus()
                }
            }

            else if (event.target.id == "ds_osl_kod") {
                if (event.keyCode == 13) {
                    $("#dsc_kod").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.ds_osl.kod = ""
                    app.$data.history.ds_osl.naim = ""
                }
                if (event.keyCode == 33) {
                    $("#dskz_kod").focus()
                }
            }

            else if (event.target.id == "dsc_kod") {
                if (event.keyCode == 13) {
                    $("#dson_kod").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.dsc.kod = ""
                    app.$data.history.dsc.naim = ""
                }
                if (event.keyCode == 33) {
                    $("#ds_osl_kod").focus()
                }
            }

            else if (event.target.id == "dson_kod") {
                if (event.keyCode == 13) {
                    $("#dat_otd").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.dson.kod = ""
                    app.$data.history.dson.naim = ""
                }
                if (event.keyCode == 33) {
                    $("#dsc_kod").focus()
                }
            }

            else if (event.target.id == "dat_otd") {
                if (event.keyCode == 13) {
                    $("#tm_otd_d").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.dat_otd = ""
                }
                if (event.keyCode == 33) {
                    $("#dson_kod").focus()
                }
            }

            else if (event.target.id == "tm_otd_d") {
                if (event.keyCode == 13) {
                    $("#icx").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.tm_otd_d = ""
                }
                if (event.keyCode == 33) {
                    $("#dat_otd").focus()
                }
            }

            else if (event.target.id == "icx") {
                if (event.keyCode == 13) {
                    $("#rslt").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.icx = ""
                }
                if (event.keyCode == 33) {
                    $("#tm_otd_d").focus()
                }
            }

            else if (event.target.id == "rslt") {
                if (event.keyCode == 13) {
                    app.next_tabs()
                }
                if (event.keyCode == 46) {
                    app.$data.history.rslt = ""
                }
                if (event.keyCode == 33) {
                    $("#icx").focus()
                }
            }

        }


        if (document.getElementById("list-profile-list_inf_koyko").classList.contains('active')) {

            // console.log(event.keyCode)
            if (event.keyCode == 19) {
                document.getElementById("list-profile-list_inf_policy_passport_snills").click()
            }

            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_koyko")) {
                next_tab()
            }

            // if (event.keyCode == 27){
            //     app.next_inf_operation()
            // }

            if (event.keyCode == 45) {
                Koyko_add()
                $('input[name="N"]').focus()


            }
            if (event.keyCode == 46) {
                if (event.target.id != "aro_n" && event.target.id != "aro_let"
                    && event.target.id != "aro_sofa" && event.target.id != "aro_ivl") {
                    if (app.$data.history.le_vr.length != 0) {
                        let tbody = document.getElementById('koyko_table').querySelector('tbody')
                        tbody.innerHTML = ''
                        app.$data.history.le_vr = []
                    }
                }
            }

            if (event.target.name == "N") {
                if (event.keyCode == 13) {
                    $('input[name="aro"]').focus()
                }
                if (event.keyCode == 8) {
                    $('input[name="N"]').val("")
                }
            }
            else if (event.target.name == "aro") {
                if (event.keyCode == 13) {
                    $('input[name="otd"]').focus()
                }
                if (event.keyCode == 8) {
                    $('input[name="aro"]').val("")
                }
            }

            else if (event.target.name == "otd") {
                if (event.keyCode == 13) {
                    $('input[name="prof_k"]').focus()
                }
                if (event.keyCode == 8) {
                    $('input[name="otd"]').val("")
                }
            }

            else if (event.target.name == "prof_k") {
                if (event.keyCode == 13) {
                    $('input[name="kod"]').focus()
                }
                if (event.keyCode == 8) {
                    $('input[name="prof_k"]').val("")
                }
            }

            else if (event.target.name == "kod") {

                if (event.keyCode == 13) {
                    if (app.$data.history.le_vr.aro.length > 0) {
                        $('#aro_n').focus()
                    }
                    else {
                        $('input[name="N"]').focus()
                    }
                }
                if (event.keyCode == 8) {
                    $('input[name="kod"]').val("")
                }
            }
            else if (event.target.id == "aro_n") {
                if (event.keyCode == 13) {
                    $('#aro_let').focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.le_vr.aro_n = ""
                }
            }
            else if (event.target.id == "aro_let") {
                if (event.keyCode == 13) {
                    $('#aro_sofa').focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.le_vr.aro_let = ""
                }
                if (event.keyCode == 33) {
                    $("#aro_n").focus()
                }
            }
            else if (event.target.id == "aro_sofa") {
                if (event.keyCode == 13) {
                    $('#aro_ivl').focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.le_vr.aro_sofa = ""
                }
                if (event.keyCode == 33) {
                    $("#aro_let").focus()
                }
            }
            else if (event.target.id == "aro_ivl") {
                if (event.keyCode == 13) {
                    $('input[name="N"]').focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.le_vr.aro_ivl = ""
                }
                if (event.keyCode == 33) {
                    $("#aro_sofa").focus()
                }
            }




            // if ((event.keyCode == 13) && (event.target.name !="N" || event.target.name!="aro" || event.target.name != "otd"
            // ||event.target.name!= "prof_k" )) {
            //     if (app.$data.history.le_vr.length != 0) {
            //         Koyko_edit()
            //         $('input[name="N"]').focus()
            //     }
            // }


            // input.value != '0' && input.value != ''
        }

        if (document.getElementById("list-profile-list_inf_operation").classList.contains('active')) {
            // if (event.keyCode == 45) {
            //     document.getElementById("add_tr_operation").click()
            //     // $('input[name="dato"]').last().focus()
            // }

            // if (event.keyCode == 27){
            //     app.next_inf_operation()
            // }
            let scrol = document.getElementById("inf_operation")
            // console.log(scrol)
            // scrol.scrollLeft = 100



            if (event.keyCode == 19) {
                document.getElementById("list-profile-list_inf_ks_zabolev").click()
            }
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_operation")) {
                next_tab()
            }

            if ((event.keyCode == 13)) {
                if (app.$data.history.le_vr.oper != 0) {
                    $('td[name="dato"] input').first().focus()
                    document.getElementById("inf_operation").scrollLeft = 0
                }
            }

            if ((event.keyCode == 13) && (event.target.id != "staticBackdrop" || event.target.id != "list-profile-list_inf_operation")) {
                let el = event.target
                // if (el.name == "goc") {
                //     scrol.scrollLeft = 400
                // }
                if (el.name == "dato") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="tm_o"]`).focus()
                }
                else if (el.name == "tm_o") {
                    $("#operation_table").find(`select[n="${parseInt(el.getAttribute("n"), 10)}"][name="py"]`).focus()
                }
                else if (el.name == "py") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="kod_op"]`).focus()

                }
                else if (el.name == "kod_op") {
                    $("#operation_table").find(`select[n="${parseInt(el.getAttribute("n"), 10)}"][name="goc"]`).focus()
                    // document.getElementById("inf_operation").scrollLeft += 1000
                    // $("#operation_table").scrollLeft(1500);


                }
                else if (el.name == "goc") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="kodx"]`).focus()
                    scrol.scrollLeft = 100
                    setTimeout(() => {
                        scrol.scrollLeft = 400
                    }, 20)


                }
                else if (el.name == "kodx") {
                    $("#operation_table").find(`select[n="${parseInt(el.getAttribute("n"), 10)}"][name="pop"]`).focus()
                    setTimeout(() => {
                        scrol.scrollLeft = 600
                    }, 20)

                }
                else if (el.name == "pop") {
                    // $("#operation_table").find(`div[n="${parseInt(el.getAttribute("n"), 10)}"][name="pr_osob"]`).focus()
                    let pr_osob = $("#operation_table").find(`div[n="${parseInt(el.getAttribute("n"), 10)}"][name="pr_osob"]`)
                    pr_osob[0].childNodes[0].childNodes[0].focus()

                    setTimeout(() => {
                        scrol.scrollLeft = 700
                    }, 20)

                }
                else if (el.name == "pr_osob") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="k_mm"]`).focus()
                    setTimeout(() => {
                        scrol.scrollLeft = 900
                    }, 20)
                }
                else if (el.name == "k_mm") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="kodxa"]`).focus()
                    setTimeout(() => {
                        scrol.scrollLeft = 1200
                    }, 20)
                }
                else if (el.name == "kodxa") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="kodxa1"]`).focus()
                    setTimeout(() => {
                        scrol.scrollLeft = 1200
                    }, 20)
                }
                else if (el.name == "kodxa1") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="obz"]`).focus()
                    setTimeout(() => {
                        scrol.scrollLeft = 1200
                    }, 20)
                }
                else if (el.name == "obz") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="obz_2"]`).focus()
                    setTimeout(() => {
                        scrol.scrollLeft = 1200
                    }, 20)
                }
                else if (el.name == "obz_2") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="kodan"]`).focus()
                    setTimeout(() => {
                        scrol.scrollLeft = 1200
                    }, 20)
                }
                else if (el.name == "kodan") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="dato"]`).focus()
                    setTimeout(() => {
                        scrol.scrollLeft = 0
                    }, 20)
                }

            }
            if ((event.keyCode == 8) && (event.target.id != "staticBackdrop" || event.target.id != "list-profile-list_inf_operation")) {
                let el = event.target

                if (el.name == "dato") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="dato"]`).val("")
                }
                else if (el.name == "tm_o") {
                    $("#operation_table").find(`select[n="${parseInt(el.getAttribute("n"), 10)}"][name="tm_o"]`).val("")
                }
                else if (el.name == "py") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="py"]`).val("")
                }
                else if (el.name == "kod_op") {
                    $("#operation_table").find(`select[n="${parseInt(el.getAttribute("n"), 10)}"][name="kod_op"]`).val("")
                }
                else if (el.name == "goc") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="goc"]`).val("")
                }
                else if (el.name == "kodx") {
                    $("#operation_table").find(`select[n="${parseInt(el.getAttribute("n"), 10)}"][name="kodx"]`).val("")
                }
                else if (el.name == "pop") {
                    $("#operation_table").find(`select[n="${parseInt(el.getAttribute("n"), 10)}"][name="pop"]`).val("")
                }
                else if (el.name == "pr_osob") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="pr_osob"]`).val("")
                }
                else if (el.name == "k_mm") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="k_mm"]`).val("")
                }
                else if (el.name == "kodxa") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="kodxa"]`).val("")
                }
                else if (el.name == "kodxa1") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="kodxa1"]`).val("")
                }
                else if (el.name == "obz") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="obz"]`).val("")
                }
                else if (el.name == "obz_2") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="obz_2"]`).val("")
                }
                else if (el.name == "kodan") {
                    $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="kodan"]`).val("")
                }

            }
            // if (event.keyCode == 46) {
            //     if (app.$data.history.oper.length != 0) {
            //         Oper_delete($(`tr[n="${event.target.getAttribute("n")}"]`)[0].childNodes[0])
            //         $('td[name="dato"] input').last().focus()
            //     }

            // }
            if (event.keyCode == 33) {
                if (app.$data.history.le_vr.oper != 0) {
                    let el = event.target
                    if (el.name != "pr_osob") {
                        let inp = $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10) - 1}"][name="${el.getAttribute("name")}"]`)
                        if (inp.length != 0) {
                            inp[0].focus()
                        }
                        else {
                            let inp = $("#operation_table").find(`select[n="${parseInt(el.getAttribute("n"), 10) - 1}"][name="${el.getAttribute("name")}"]`)
                            if (inp.length != 0) {
                                inp[0].focus()
                            }
                        }
                    }
                    else {
                        let inp = $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="${el.getAttribute("name")}"][nn="${el.getAttribute("nn")}"]`)
                        if (inp[0].getAttribute("nn") != "0") {
                            $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="${el.getAttribute("name")}"][nn="${parseInt(el.getAttribute("nn"), 10) - 1}"]`)[0].focus()
                        }
                        else {
                            $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="${el.getAttribute("name")}"][nn="${parseInt(el.getAttribute("nn"), 10) + 8}"]`)[0].focus()
                        }
                    }

                }
            }
            if (event.keyCode == 34) {
                if (app.$data.history.le_vr.oper != 0) {
                    let el = event.target
                    if (el.name != "pr_osob") {
                        let inp = $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10) + 1}"][name="${el.getAttribute("name")}"]`)
                        if (inp.length != 0) {
                            inp[0].focus()
                        }
                        else {
                            let inp = $("#operation_table").find(`select[n="${parseInt(el.getAttribute("n"), 10) + 1}"][name="${el.getAttribute("name")}"]`)
                            if (inp.length != 0) {
                                inp[0].focus()
                            }
                        }
                    }
                    else {
                        let inp = $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="${el.getAttribute("name")}"][nn="${el.getAttribute("nn")}"]`)
                        if (inp[0].getAttribute("nn") != "8") {
                            $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="${el.getAttribute("name")}"][nn="${parseInt(el.getAttribute("nn"), 10) + 1}"]`)[0].focus()
                        }
                        else {
                            $("#operation_table").find(`input[n="${parseInt(el.getAttribute("n"), 10)}"][name="${el.getAttribute("name")}"][nn="${parseInt(el.getAttribute("nn"), 10) - 8}"]`)[0].focus()
                        }
                    }

                }
            }


        }

        if (document.getElementById("list-profile-list_inf_ks_zabolev").classList.contains('active')) {
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_ks_zabolev")) {
                next_tab()
            }
            if (event.keyCode == 19) {
                let ks_zabolev = $("#inf_ks_zabolev").find('input[type=text]')
                for (ks of ks_zabolev) {
                    ks.blur()
                }
            }
            if (app.history.vds != 'ВТМП баз.программа ОМС' && app.history.vds != 'ВТМП сверхбаз.программа') {
                if (event.target.id == "ksg_osn") {
                    if (event.keyCode == 13) {
                        $("#oopkk").focus()
                    }
                    if (event.keyCode == 46) {
                        app.$data.history.ksg_osn = ""
                    }
                }
                else if (event.target.id == "oopkk") {
                    if (event.keyCode == 13) {
                        $("#ksg_sop").focus()
                    }
                    if (event.keyCode == 46) {
                        app.$data.history.oopkk = ""
                    }
                    if (event.keyCode == 33) {
                        $("#ksg_osn").focus()
                    }
                }
                else if (event.target.id == "ksg_sop") {
                    if (event.keyCode == 13) {
                        $("#iddoc").focus()
                    }
                    if (event.keyCode == 46) {
                        app.$data.history.ksg_sop = ""
                    }
                    if (event.keyCode == 33) {
                        $("#oopkk").focus()
                    }
                }
                else if (event.target.id == "iddoc") {
                    if (event.keyCode == 13) {

                    }
                    if (event.keyCode == 46) {
                        app.$data.history.iddoc = ""
                    }
                    if (event.keyCode == 33) {
                        $("#ksg_sop").focus()
                    }
                }
            }
            else {
                if (event.target.id == "metod_hmp") {
                    if (event.keyCode == 13) {
                        $("#vid_hmp").focus()
                    }
                    if (event.keyCode == 46) {
                        app.$data.history.metod_hmp = ""
                    }
                }
                if (event.target.id == "vid_hmp") {
                    if (event.keyCode == 46) {
                        app.$data.history.vid_hmp = ""
                    }
                }

            }
        }

        if (document.getElementById("list-profile-list_inf_complication").classList.contains('active')) {
            if (event.keyCode == 19) {
                document.getElementById("list-profile-list_inf_complication").click()
            }

            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_complication")) {
                next_tab()
            }

            if ((event.keyCode == 13) && (event.target.id == "staticBackdrop" || event.target.id == "list-profile-list_inf_complication")) {
                $('select[name="inf_oper"]').first().focus()
            }

            if ((event.keyCode == 13) && (event.target.id != "staticBackdrop" || event.target.id != "list-profile-list_inf_complication")) {
                let el = event.target

                if (el.name == "inf_oper") {
                    $("#complication_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10)}"][name="tnvr"]`).focus()
                }
                else if (el.name == "tnvr") {
                    $("#complication_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10)}"][name="dato"]`).focus()
                }
                else if (el.name == "dato") {
                    $("#complication_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10)}"][name="osl"]`).focus()
                }
                else if (el.name == "osl") {
                    $("#complication_table").find(`select[tr="${parseInt(el.getAttribute("tr"), 10)}"][name="xosl"]`).focus()
                }
                else if (el.name == "xosl") {
                    $("#complication_table").find(`select[tr="${parseInt(el.getAttribute("tr"), 10)}"][name="posl"]`).focus()
                }
                else if (el.name == "posl") {
                    $("#complication_table").find(`select[tr="${parseInt(el.getAttribute("tr"), 10)}"][name="aosl"]`).focus()
                }
                else if (el.name == "aosl") {
                    $("#complication_table").find(`select[tr="${parseInt(el.getAttribute("tr"), 10)}"][name="inf_oper"]`).focus()
                }
            }


            // if (event.keyCode == 45) {
            //     // Complication_add()
            //     document.getElementById("add_tr_complication").click()
            //     // $('select[name="inf_oper"]').last().focus()
            // }
            // if (event.keyCode == 46) {
            //     if (app.$data.history.oslo.length != 0) {
            //         Complication_delete($(`tr[n="${event.target.getAttribute("tr")}"]`)[0].childNodes[0])
            //         $('select[name="inf_oper"]').last().focus()
            //     }
            // }

            if (event.keyCode == 33) {
                let el = event.target
                let inp = $("#complication_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10) - 1}"][name="${el.getAttribute("name")}"]`)
                if (inp.length != 0) {
                    inp[0].focus()
                }
                else {
                    let inp = $("#complication_table").find(`select[tr="${parseInt(el.getAttribute("tr"), 10) - 1}"][name="${el.getAttribute("name")}"]`)
                    if (inp.length != 0) {
                        inp[0].focus()
                    }
                }

            }

            if (event.keyCode == 34) {
                let el = event.target
                let inp = $("#complication_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10) + 1}"][name="${el.getAttribute("name")}"]`)
                if (inp.length != 0) {
                    inp[0].focus()
                }
                else {
                    let inp = $("#complication_table").find(`select[tr="${parseInt(el.getAttribute("tr"), 10) + 1}"][name="${el.getAttribute("name")}"]`)
                    if (inp.length != 0) {
                        inp[0].focus()
                    }
                }
            }
        }

        if (document.getElementById("list-profile-list_inf_work_capacity").classList.contains('active')) {
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_work_capacity")) {
                next_tab()
            }
            if (event.keyCode == 19) {
                // document.getElementById("list-profile-list_inf_work_capacity").click()
            }
        }

        if (document.getElementById("list-profile-list_inf_manipulation").classList.contains('active')) {
            if (event.keyCode == 19) {
                document.getElementById("list-home-list_inf_pers_info").click()
            }
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_manipulation")) {
                next_tab()
            }


            if ((event.keyCode == 13) && (event.target.id == "staticBackdrop" || event.target.id == "list-profile-list_inf_manipulation")) {
                $('input[name="datm"]').first().focus()
            }

            if ((event.keyCode == 13) && (event.target.id != "staticBackdrop" || event.target.id != "list-profile-list_inf_manipulation")) {
                let el = event.target

                if (el.name == "datm") {
                    $("#manipulation_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10)}"][name="tnvr"]`).focus()
                }
                else if (el.name == "tnvr") {
                    $("#manipulation_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10)}"][name="kodmn"]`).focus()
                }
                else if (el.name == "kodmn") {
                    $("#manipulation_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10)}"][name="kol"]`).focus()
                }
                else if (el.name == "kol") {
                    // $("#manipulation_table").find(`select[tr="${parseInt(el.getAttribute("tr"), 10)}"][name="pl"]`).focus()
                    $("#manipulation_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10)}"][name="datm"]`).focus()
                }
                // else if (el.name == "pl") {
                //     $("#manipulation_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10)}"][name="datm"]`).focus()
                // }
            }

            // if (event.keyCode == 45) {
            //     document.getElementById("add_tr_manipulation").click()
            //     // $('input[name="datm"]').last().focus()
            // }
            // if (event.keyCode == 46) {
            //     if (app.$data.history.manipulation.length != 0) {
            //         Manipulation_delete($(`tr[n="${event.target.getAttribute("tr")}"]`)[0].childNodes[0])
            //         $('input[name="datm"]').last().focus()
            //     }
            // }

            if (event.keyCode == 33) {
                let el = event.target
                let inp = $("#manipulation_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10) - 1}"][name="${el.getAttribute("name")}"]`)
                if (inp.length != 0) {
                    inp[0].focus()
                }
                else {
                    let inp = $("#manipulation_table").find(`select[tr="${parseInt(el.getAttribute("tr"), 10) - 1}"][name="${el.getAttribute("name")}"]`)
                    if (inp.length != 0) {
                        inp[0].focus()
                    }
                }

            }

            if (event.keyCode == 34) {
                let el = event.target
                let inp = $("#manipulation_table").find(`input[tr="${parseInt(el.getAttribute("tr"), 10) + 1}"][name="${el.getAttribute("name")}"]`)
                if (inp.length != 0) {
                    inp[0].focus()
                }
                else {
                    let inp = $("#manipulation_table").find(`select[tr="${parseInt(el.getAttribute("tr"), 10) + 1}"][name="${el.getAttribute("name")}"]`)
                    if (inp.length != 0) {
                        inp[0].focus()
                    }
                }
            }
        }

        if (document.getElementById("list-profile-list_inf_translations").classList.contains('active')) {
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_translations")) {
                next_tab()
            }
            if (event.keyCode == 19) {
                let translations = $("#inf_translations").find('input[type=text]')
                for (t of translations) {
                    t.blur()
                }
            }
            if (event.target.id == "potd") {
                if (event.keyCode == 13) {
                    $("#dat_pe").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.potd = ""
                }
            }
            else if (event.target.id == "dat_pe") {
                if (event.keyCode == 13) {
                    $("#kod_y").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.dat_pe = ""
                }
                if (event.keyCode == 33) {
                    $("#potd").focus()
                }
            }
            else if (event.target.id == "kod_y") {
                if (event.keyCode == 13) {
                    $("#pr_per").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.kod_y = ""
                }
                if (event.keyCode == 33) {
                    $("#dat_pe").focus()
                }
            }
            else if (event.target.id == "pr_per") {
                if (event.keyCode == 46) {
                    app.$data.history.pr_per = ""
                }
                if (event.keyCode == 13) {
                    app.next_inf_koyko()
                }
                if (event.keyCode == 33) {
                    $("#kod_y").focus()
                }
            }


        }

        if (document.getElementById("list-profile-list_inf_post_mortem").classList.contains('active')) {
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_post_mortem")) {
                next_tab()
            }
            if (event.keyCode == 19) {
                let post_mortem = $("#inf_post_mortem").find('input[type=text]')
                for (p of post_mortem) {
                    p.blur()
                }
            }
            if (event.target.id == "wskr_date") {
                if (event.keyCode == 13) {
                    $("#tm_let").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.wskr_date = ""
                }
            }
            else if (event.target.id == "tm_let") {
                if (event.keyCode == 13) {
                    $("#pri").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.tm_let = ""
                }
                if (event.keyCode == 33) {
                    $("#wskr_date").focus()
                }
            }
            else if (event.target.id == "pri") {
                if (event.keyCode == 13) {
                    $("#ds_let_kod").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.pri = ""
                }
                if (event.keyCode == 33) {
                    $("#tm_let").focus()
                }
            }
            else if (event.target.id == "ds_let_kod") {
                if (event.keyCode == 13) {
                    $("#wskr").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.ds_let.kod = ""
                    app.$data.history.ds_let.naim = ""
                }
                if (event.keyCode == 33) {
                    $("#pri").focus()
                }
            }
            else if (event.target.id == "wskr") {
                if (event.keyCode == 13) {
                    $("#dspat_kod").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.wskr = ""
                }
                if (event.keyCode == 33) {
                    $("#ds_let_kod").focus()
                }
            }
            else if (event.target.id == "dspat_kod") {
                if (event.keyCode == 13) {
                    $("#rasxp").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.dspat.kod = ""
                    app.$data.history.dspat.naim = ""
                }
                if (event.keyCode == 33) {
                    $("#wskr").focus()
                }
            }
            else if (event.target.id == "rasxp") {
                if (event.keyCode == 13) {
                    $("#otd_y").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.rasxp = ""
                }
                if (event.keyCode == 33) {
                    $("#dspat_kod").focus()
                }
            }
            else if (event.target.id == "otd_y") {
                if (event.keyCode == 13) {
                    app.next_tabs()
                }
                if (event.keyCode == 46) {
                    app.$data.history.otd_y = ""
                }
                if (event.keyCode == 33) {
                    $("#rasxp").focus()
                }
            }

        }
        if (document.getElementById("list-profile-list_inf_injury").classList.contains('active')) {
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_injury")) {
                next_tab()
            }
            if (event.keyCode == 19) {
                let injury = $("#inf_injury").find('input[type=text]')
                for (i of injury) {
                    i.blur()
                }
            }

            if (event.target.id == "dskz_kod") {
                if (event.keyCode == 13) {
                    $("#details_kod").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.dskz.kod = ""
                    app.$data.history.dskz.naim = ""
                }

            }
            else if (event.target.id == "details_kod") {
                if (event.keyCode == 13) {
                    $("#t_trv").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.details.kod = ""
                    app.$data.history.details.naim = ""
                }
                if (event.keyCode == 33) {
                    $(".dskz_kod").focus()
                }
            }
            else if (event.target.id == "t_trv") {
                if (event.keyCode == 13) {
                    $("#trav_ns").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.t_trv = ""
                }
                if (event.keyCode == 33) {
                    $("#details_kod").focus()
                }
            }
            else if (event.target.id == "trav_ns") {
                if (event.keyCode == 46) {
                    app.$data.history.trav_ns = ""
                }
                if (event.keyCode == 33) {
                    $("#t_trv").focus()
                }
            }
        }

        if (document.getElementById("list-profile-list_inf_policy_passport_snills").classList.contains('active')) {
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_policy_passport_snills")) {
                next_tab()
            }
            if (event.keyCode == 19) {
                let p = $("#inf_policy_passport_snills").find('input[type=text]')
                for (s of p) {
                    s.blur()
                }
            }
            if (event.target.id == "vds") {
                if (event.keyCode == 13) {
                    $("#sctp").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.vds = ""
                }
            }
            else if (event.target.id == "sctp") {
                if (event.keyCode == 13) {
                    $("#nctp").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.sctp = ""
                }
                if (event.keyCode == 33) {
                    $("#vds").focus()
                }
            }
            else if (event.target.id == "nctp") {
                if (event.keyCode == 13) {
                    $("#ctkom").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.nctp = ""
                }
                if (event.keyCode == 33) {
                    $("#sctp").focus()
                }
            }
            else if (event.target.id == "ctkom") {
                if (event.keyCode == 13) {
                    $("#t_pol").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.ctkom = ""
                }
                if (event.keyCode == 33) {
                    $("#nctp").focus()
                }
            }
            else if (event.target.id == "t_pol") {
                if (event.keyCode == 13) {
                    $("#udl").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.t_pol = ""
                }
                if (event.keyCode == 33) {
                    $("#ctkom").focus()
                }
            }
            else if (event.target.id == "udl") {
                if (event.keyCode == 13) {
                    $("#s_pasp").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.udl = ""
                }
                if (event.keyCode == 33) {
                    $("#t_pol").focus()
                }
            }
            else if (event.target.id == "s_pasp") {
                if (event.keyCode == 13) {
                    $("#n_pasp").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.s_pasp = ""
                }
                if (event.keyCode == 33) {
                    $("#udl").focus()
                }
            }
            else if (event.target.id == "n_pasp") {
                if (event.keyCode == 13) {
                    $("#docdate").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.n_pasp = ""
                }
                if (event.keyCode == 33) {
                    $("#s_pasp").focus()
                }
            }
            else if (event.target.id == "docdate") {
                if (event.keyCode == 13) {
                    $("#docorg").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.docdate = ""
                }
                if (event.keyCode == 33) {
                    $("#n_pasp").focus()
                }
            }
            else if (event.target.id == "docorg") {
                if (event.keyCode == 13) {
                    $(".m_roj").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.docorg = ""
                }
                if (event.keyCode == 33) {
                    $("#docdate").focus()
                }
            }
            else if (event.target.id == "m_roj") {
                if (event.keyCode == 13) {
                    $("#ss").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.m_roj = ""
                }
                if (event.keyCode == 33) {
                    $("#docorg").focus()
                }
            }
            else if (event.target.id == "ss") {
                if (event.keyCode == 46) {
                    app.$data.history.ss = ""
                }
                if (event.keyCode == 13) {
                    document.getElementById("list-home-list_inf_pers_info").click()

                }
                if (event.keyCode == 33) {
                    $("#m_roj").focus()
                }

            }

        }

        if (document.getElementById("list-profile-list_inf_pregnancy").classList.contains('active')) {
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_pregnancy")) {
                next_tab()
            }
            if (event.keyCode == 19) {
                let preg = $("#inf_pregnancy").find('input[type=text]')
                for (pr of preg) {
                    pr.blur()
                }
            }
            if (event.target.id == "vb_a_datv") {
                if (event.keyCode == 13) {
                    $("#srber").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.vb_a_datv = ""
                }
            }
            else if (event.target.id == "srber") {
                if (event.keyCode == 13) {
                    $("#n_ber").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.srber = ""
                }
                if (event.keyCode == 33) {
                    $("#vb_a_datv").focus()
                }
            }
            else if (event.target.id == "n_ber") {
                if (event.keyCode == 13) {
                    $("#pria").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.n_ber = ""
                }
                if (event.keyCode == 33) {
                    $("#srber").focus()
                }
            }
            else if (event.target.id == "pria") {
                if (event.keyCode == 13) {
                    $("#m_prer").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.pria = ""
                }
                if (event.keyCode == 33) {
                    $("#n_ber").focus()
                }
            }
            else if (event.target.id == "m_prer") {
                if (event.keyCode == 13) {
                    app.next_tabs()
                }
                if (event.keyCode == 46) {
                    app.$data.history.m_prer = ""
                }
                if (event.keyCode == 33) {
                    $("#pria").focus()
                }
            }
        }

        if (document.getElementById("list-profile-list_inf_disability").classList.contains('active')) {
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_disability")) {
                next_tab()
            }

            if (event.keyCode == 19) {
                let disability = $("#inf_disability").find('input[type=text]')
                for (di of disability) {
                    di.blur()
                }
            }

            if (event.target.id == "dat_l1") {
                if (event.keyCode == 13) {
                    $("#dat_l2").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.dat_l1 = ""
                }
            }
            else if (event.target.id == "dat_l2") {
                if (event.keyCode == 13) {
                    $("#ot_ln").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.dat_l2 = ""
                }
                if (event.keyCode == 33) {
                    $("#dat_l1").focus()
                }
            }
            else if (event.target.id == "ot_ln") {
                if (event.keyCode == 13) {
                    $("#vs_bol").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.ot_ln = ""
                }
                if (event.keyCode == 33) {
                    $("#dat_l2").focus()
                }
            }
            else if (event.target.id == "vs_bol") {
                if (event.keyCode == 13) {
                    $("#dis_sex_bol").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.vs_bol = ""
                }
                if (event.keyCode == 33) {
                    $("#ot_ln").focus()
                }
            }
            else if (event.target.id == "dis_sex_bol") {
                if (event.keyCode == 46) {
                    app.$data.history.dis_sex_bol = ""
                }
                if (event.keyCode == 33) {
                    $("#vs_bol").focus()
                }
            }
        }

        if (document.getElementById("list-profile-list_inf_patient_p").classList.contains('active')) {
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_patient_p")) {
                next_tab()
            }
            if (event.keyCode == 19) {
                let patient_p = $("#inf_patient_p").find('input[type=text]')
                for (pp of patient_p) {
                    pp.blur()
                }
            }
            if (event.target.id == "fam_p") {
                if (event.keyCode == 13) {
                    $("#im_p").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.fam_p = ""
                }
            }
            else if (event.target.id == "im_p") {
                if (event.keyCode == 13) {
                    $("#ot_p").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.im_p = ""
                }
                if (event.keyCode == 33) {
                    $("#fam_p").focus()
                }
            }
            else if (event.target.id == "ot_p") {
                if (event.keyCode == 13) {
                    $("#sex_bol").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.ot_p = ""
                }
                if (event.keyCode == 33) {
                    $("#im_p").focus()
                }
            }
            else if (event.target.id == "sex_bol") {
                if (event.keyCode == 13) {
                    $("#mp_roj").focus()
                    app.$data.history.mp_roj = $("#mp_roj").val()
                    app.$data.history.okatog_p = $("#mp_roj").attr("data-kladr-id")
                    app.$data.history.okatop_p = $("#mp_roj").attr("data-kladr-id")
                }
                if (event.keyCode == 46) {
                    app.$data.history.sex_bol = ""
                }
                if (event.keyCode == 33) {
                    $("#ot_p").focus()
                }

            }
            else if (event.target.id == "mp_roj") {
                if (event.keyCode == 13) {
                    $("#udl_p").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.mp_roj = ""
                    app.$data.history.okatog_p = ""
                    app.$data.history.okatop_p = ""
                }
                if (event.keyCode == 33) {
                    $("#sex_bol").focus()
                }
            }
            else if (event.target.id == "udl_p") {
                if (event.keyCode == 13) {
                    $("#sp_pasp").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.udl_p = ""
                }
                if (event.keyCode == 33) {
                    $("#mp_roj").focus()
                }
            }
            else if (event.target.id == "sp_pasp") {
                if (event.keyCode == 13) {
                    $("#np_pasp").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.sp_pasp = ""
                }
                if (event.keyCode == 33) {
                    $("#udl_p").focus()
                }
            }
            else if (event.target.id == "np_pasp") {
                if (event.keyCode == 13) {
                    $("#skom_p").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.np_pasp = ""
                }
                if (event.keyCode == 33) {
                    $("#sp_pasp").focus()
                }
            }
            else if (event.target.id == "skom_p") {
                if (event.keyCode == 13) {
                    $("#stat_p").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.skom_p = ""
                }
                if (event.keyCode == 33) {
                    $("#np_pasp").focus()
                }
            }
            else if (event.target.id == "stat_p") {
                if (event.keyCode == 13) {
                    $("#s_pol").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.stat_p = ""
                }
                if (event.keyCode == 33) {
                    $("#skom_p").focus()
                }
            }
            else if (event.target.id == "s_pol") {
                if (event.keyCode == 13) {
                    $("#n_pol").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.s_pol = ""
                }
                if (event.keyCode == 33) {
                    $("#stat_p").focus()
                }
            }
            else if (event.target.id == "n_pol") {
                if (event.keyCode == 46) {
                    app.$data.history.n_pol = ""
                }
                if (event.keyCode == 33) {
                    $("#s_pol").focus()
                }
            }
        }

        if (document.getElementById("list-profile-list_inf_adr").classList.contains('active')) {

            if (event.target.id == "c_oksm_in") {
                if (event.keyCode == 13) {
                    $("#m_roj_in").focus()
                    $("#m_roj_in").change(function () {
                        app.$data.history.m_roj = $("#m_roj_in").val()
                        app.$data.history.okatog = $("#m_roj_in").attr("data-kladr-id")
                    })
                }
                if (event.keyCode == 46) {
                    console.log('123d')
                    app.$data.history.c_oksm_in = ""
                    document.getElementById("c_oksm_in").value = ""
                }
            }
            else if (event.target.id == "m_roj_in") {
                if (event.keyCode == 13) {
                    $("#kv_in").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.m_roj_in = ""
                    document.getElementById("m_roj_in").value = ""
                }
                if (event.keyCode == 33) {
                    $("#c_oksm_in").focus()
                }
            }
            else if (event.target.id == "kv_in") {
                if (event.keyCode == 13) {
                    $("#kp_in").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.kv_in = ""
                    document.getElementById("kv_in").value = ""
                }
                if (event.keyCode == 33) {
                    $("#m_roj_in").focus()
                }
            }
            else if (event.target.id == "kp_in") {
                if (event.keyCode == 13) {
                    $("#stro_in").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.kp_in = ""
                    document.getElementById("kp_in").value = ""
                }
                if (event.keyCode == 33) {
                    $("#kv_in").focus()
                }
            }
            else if (event.target.id == "stro_in") {
                if (event.keyCode == 13) {
                    $("#cj_in").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.stro_in = ""
                    document.getElementById("stro_in").value = ""
                }
                if (event.keyCode == 33) {
                    $("#kp_in").focus()
                }
            }
            else if (event.target.id == "cj_in") {
                if (event.keyCode == 13) {
                    $("#rai_in").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.cj_in = ""
                    document.getElementById("cj_in").value = ""
                }
                if (event.keyCode == 33) {
                    $("#stro_in").focus()
                }
            }
            else if (event.target.id == "rai_in") {
                if (event.keyCode == 13) {
                    document.getElementById("list-home-list_inf_pers_info").click()
                    setTimeout(() => {
                        $("#adr_in").focus()
                        $("#adr_in").change(function () {
                            app.$data.history.adr = $("#adr_in").val()
                            app.$data.history.okatop = $("#adr_in").attr("data-kladr-id")
                        })
                    }, 1200)

                }
                if (event.keyCode == 46) {
                    app.$data.history.rai_in = ""
                    document.getElementById("rai_in").value = ""
                }
                if (event.keyCode == 33) {
                    $("#cj_in").focus()
                }
            }
        }

        if (document.getElementById("list-profile-list_inf_onmk").classList.contains('active')) {
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_onmk")) {
                next_tab()
            }
            if (event.keyCode == 19) {
                document.getElementById("list-profile-list_inf_onmk").click()
            }
        }

        if (document.getElementById("list-profile-list_inf_onk").classList.contains('active')) {
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_onk")) {
                next_tab()
            }
            let scrol = document.getElementById("inf_onk_scrol")


            if (event.keyCode == 19) {
                let onk = $("#inf_onk").find('input[type=text]')
                for (o of onk) {
                    o.blur()
                }
            }

            if (event.target.id == "ds1_t") {
                if (event.keyCode == 13) {
                    $("#stad").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.ds1_t = ""
                }
            }
            else if (event.target.id == "stad") {
                if (event.keyCode == 13) {
                    $("#onk_t").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.stad = ""
                }
                if (event.keyCode == 33) {
                    $("#ds1_t").focus()
                }
            }
            else if (event.target.id == "onk_t") {
                if (event.keyCode == 13) {
                    $("#onk_n").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.onk_t = ""
                }
                if (event.keyCode == 33) {
                    $("#stad").focus()
                }
            }
            else if (event.target.id == "onk_n") {
                if (event.keyCode == 13) {
                    $("#onk_m").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.onk_n = ""
                }
                if (event.keyCode == 33) {
                    $("#onk_t").focus()
                }
            }
            else if (event.target.id == "onk_m") {
                if (event.keyCode == 13) {
                    $("#mtstz").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.onk_m = ""
                }
                if (event.keyCode == 33) {
                    $("#onk_n").focus()
                }
            }
            else if (event.target.id == "mtstz") {
                if (event.keyCode == 13) {
                    $("#c_zab").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.mtstz = ""
                }
                if (event.keyCode == 33) {
                    $("#onk_m").focus()
                }
            }
            else if (event.target.id == "c_zab") {
                if (event.keyCode == 13) {
                    $("#diag_date").focus()
                    setTimeout(() => {
                        scrol.scrollTop = 150
                    }, 20)
                }
                if (event.keyCode == 46) {
                    app.$data.history.c_zab = ""
                }
                if (event.keyCode == 33) {
                    $("#mtstz").focus()
                }
            }
            else if (event.target.id == "diag_date") {
                if (event.keyCode == 13) {
                    $("#diag_tip").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.diag_date = ""
                }
                if (event.keyCode == 33) {
                    $("#c_zab").focus()
                }
            }
            else if (event.target.id == "diag_tip") {
                if (event.keyCode == 13) {
                    $("#diag_code").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.diag_tip = ""
                }
                if (event.keyCode == 33) {
                    $("#diag_date").focus()
                }
            }
            else if (event.target.id == "diag_code") {
                if (event.keyCode == 13) {
                    $("#diag_rslt").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.diag_code = ""
                }
                if (event.keyCode == 33) {
                    $("#diag_tip").focus()
                }
            }
            else if (event.target.id == "diag_rslt") {
                if (event.keyCode == 13) {
                    $("#rec_rslt").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.diag_rslt = ""
                }
                if (event.keyCode == 33) {
                    $("#diag_code").focus()
                }
            }
            else if (event.target.id == "rec_rslt") {
                if (event.keyCode == 13) {
                    $("#dt_cons").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.rec_rslt = ""
                }
                if (event.keyCode == 33) {
                    $("#diag_rslt").focus()
                }
            }
            else if (event.target.id == "dt_cons") {
                if (event.keyCode == 13) {
                    $("#pr_cons").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.dt_cons = ""
                }
                if (event.keyCode == 33) {
                    $("#rec_rslt").focus()
                }
            }
            else if (event.target.id == "pr_cons") {
                if (event.keyCode == 13) {
                    $("#usl_tip").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.pr_cons = ""
                }
                if (event.keyCode == 33) {
                    $("#dt_cons").focus()
                }
            }
            else if (event.target.id == "usl_tip") {
                if (event.keyCode == 13) {
                    $("#hir_tip").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.usl_tip = ""
                }
                if (event.keyCode == 33) {
                    $("#pr_cons").focus()
                }
            }
            else if (event.target.id == "hir_tip") {
                if (event.keyCode == 13) {
                    $("#d_prot").focus()
                    setTimeout(() => {
                        scrol.scrollTop = 1050
                    }, 20)
                }
                if (event.keyCode == 46) {
                    app.$data.history.hir_tip = ""
                }
                if (event.keyCode == 33) {
                    $("#usl_tip").focus()
                }
            }
            else if (event.target.id == "d_prot") {
                if (event.keyCode == 13) {
                    $("#prot").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.d_prot = ""
                }
                if (event.keyCode == 33) {
                    $("#hir_tip").focus()
                }
            }
            else if (event.target.id == "prot") {
                if (event.keyCode == 13) {
                    $("#naprdate").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.prot = ""
                }
                if (event.keyCode == 33) {
                    $("#d_prot").focus()
                }
            }
            else if (event.target.id == "naprdate") {
                if (event.keyCode == 13) {
                    $("#napr_v").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.naprdate = ""
                }
                if (event.keyCode == 33) {
                    $("#prot").focus()
                }
            }
            else if (event.target.id == "napr_v") {
                if (event.keyCode == 13) {
                    $("#napr_mo").focus()
                }

                if (event.keyCode == 46) {
                    app.$data.history.napr_v = ""
                }
                if (event.keyCode == 33) {
                    $("#naprdate").focus()
                }
            }
            else if (event.target.id == "napr_mo") {
                if (event.keyCode == 13) {
                    $("#napr_issl").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.napr_mo = ""
                }
                if (event.keyCode == 33) {
                    $("#napr_v").focus()
                }
            }
            else if (event.target.id == "napr_issl") {
                if (event.keyCode == 13) {
                    $("#napr_usl").focus()
                }
                if (event.keyCode == 46) {
                    app.$data.history.napr_issl = ""
                }
                if (event.keyCode == 33) {
                    $("#napr_mo").focus()
                }
            }
            else if (event.target.id == "napr_usl") {
                if (event.keyCode == 13) {
                    app.next_tabs()
                }
                if (event.keyCode == 46) {
                    app.$data.history.napr_usl = ""
                }
                if (event.keyCode == 33) {
                    $("#napr_issl").focus()
                }
            }
        }

        if (document.getElementById("list-profile-list_inf_mo").classList.contains('active')) {
            if ((event.target.id == "staticBackdrop") || (event.target.id == "list-profile-list_inf_mo")) {
                next_tab()
            }
            if (event.keyCode == 19) {
                let mo = $("#inf_mo").find('input[type=text]')
                for (m of mo) {
                    m.blur()
                }
            }
            if (event.keyCode == 46) {
                app.$data.history.pmg = ""
            }
        }


    })
}



function mask() {
    // let input_datp = document.getElementById("datp")
    // input_datp.setAttribute("maxlength", 10)
    // input_datp.addEventListener("input", function () {
    //     var n = input_datp.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_datp.value = n.join('')
    // })

    // let input_tm_otd = document.getElementById("tm_otd")
    // input_tm_otd.setAttribute("maxlength", 5)
    // input_tm_otd.addEventListener("input", function () {
    //     var n = input_tm_otd.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, ':')
    //     input_tm_otd.value = n.join('')
    // })

    // let input_datv = document.getElementById("datv")
    // input_datv.setAttribute("maxlength", 10)
    // input_datv.addEventListener("input", function () {
    //     var n = input_datv.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_datv.value = n.join('')
    // })

    // let input_datr = document.getElementById("datr")
    // input_datr.setAttribute("maxlength", 10)
    // input_datr.addEventListener("input", function () {
    //     var n = input_datr.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_datr.value = n.join('')
    // })

    // let input_npr_date = document.getElementById("npr_date")
    // input_npr_date.setAttribute("maxlength", 10)
    // input_npr_date.addEventListener("input", function () {
    //     var n = input_npr_date.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_npr_date.value = n.join('')
    // })

    // let input_dat_otd = document.getElementById("dat_otd")
    // input_dat_otd.setAttribute("maxlength", 10)
    // input_dat_otd.addEventListener("input", function () {
    //     var n = input_dat_otd.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_dat_otd.value = n.join('')
    // })

    // let input_tm_otd_d = document.getElementById("tm_otd_d")
    // input_tm_otd_d.setAttribute("maxlength", 5)
    // input_tm_otd_d.addEventListener("input", function () {
    //     var n = input_tm_otd_d.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, ':')
    //     input_tm_otd_d.value = n.join('')
    // })

    // let input_dat_pe = document.getElementById("dat_pe")
    // input_dat_pe.setAttribute("maxlength", 10)
    // input_dat_pe.addEventListener("input", function () {
    //     var n = input_dat_pe.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_dat_pe.value = n.join('')
    // })

    // let input_wskr_date = document.getElementById("wskr_date")
    // input_wskr_date.setAttribute("maxlength", 10)
    // input_wskr_date.addEventListener("input", function () {
    //     var n = input_wskr_date.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_wskr_date.value = n.join('')
    // })


    // let input_tm_let = document.getElementById("tm_let")
    // input_tm_let.setAttribute("maxlength", 5)
    // input_tm_let.addEventListener("input", function () {
    //     var n = input_tm_let.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, ':')
    //     input_tm_let.value = n.join('')
    // })

    // let input_docdate = document.getElementById("docdate")
    // input_docdate.setAttribute("maxlength", 10)
    // input_docdate.addEventListener("input", function () {
    //     var n = input_docdate.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_docdate.value = n.join('')
    // })

    // let input_ss = document.getElementById("ss")
    // input_ss.setAttribute("maxlength", 14)
    // input_ss.addEventListener("input", function () {
    //     var n = input_ss.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 3) n.splice(3, 0, '-')
    //     if (n.length > 7) n.splice(7, 0, '-')
    //     if (n.length > 11) n.splice(11, 0, ' ')
    //     input_ss.value = n.join('')
    // })


    // let input_vb_a_datv = document.getElementById("vb_a_datv")
    // input_vb_a_datv.setAttribute("maxlength", 10)
    // input_vb_a_datv.addEventListener("input", function () {
    //     var n = input_vb_a_datv.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_vb_a_datv.value = n.join('')
    // })

    // let input_dat_l1 = document.getElementById("dat_l1")
    // input_dat_l1.setAttribute("maxlength", 10)
    // input_dat_l1.addEventListener("input", function () {
    //     var n = input_dat_l1.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_dat_l1.value = n.join('')
    // })

    // let input_dat_l2 = document.getElementById("dat_l2")
    // input_dat_l2.setAttribute("maxlength", 10)
    // input_dat_l2.addEventListener("input", function () {
    //     var n = input_dat_l2.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_dat_l2.value = n.join('')
    // })

    // let input_diag_date = document.getElementById("diag_date")
    // input_diag_date.setAttribute("maxlength", 10)
    // input_diag_date.addEventListener("input", function () {
    //     var n = input_diag_date.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_diag_date.value = n.join('')
    // })

    // let input_dt_cons = document.getElementById("dt_cons")
    // input_dt_cons.setAttribute("maxlength", 10)
    // input_dt_cons.addEventListener("input", function () {
    //     var n = input_dt_cons.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_dt_cons.value = n.join('')
    // })

    // let input_d_prot = document.getElementById("d_prot")
    // input_d_prot.setAttribute("maxlength", 10)
    // input_d_prot.addEventListener("input", function () {
    //     var n = input_d_prot.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_d_prot.value = n.join('')
    // })

    // let input_naprdate = document.getElementById("naprdate")
    // input_naprdate.setAttribute("maxlength", 10)
    // input_naprdate.addEventListener("input", function () {
    //     var n = input_naprdate.value.replace(/[^0-9]/g, '').split('')
    //     if (n.length > 2) n.splice(2, 0, '-')
    //     if (n.length > 4) n.splice(5, 0, '-')
    //     input_naprdate.value = n.join('')
    // })
}
function next_tab() {
    if (stop_tab() && (event.target.type != "text")) {
        if (event.keyCode === 49 || event.keyCode === 97) {
            document.getElementById("list-home-list_inf_pers_info").click()
        }
        else if (event.keyCode === 50 || event.keyCode === 98) {
            document.getElementById("list-profile-list_inf_diagnoses").click()
        }
        else if (event.keyCode === 51 || event.keyCode === 99) {
            document.getElementById("list-profile-list_inf_koyko").click()
        }
        else if (event.keyCode === 52 || event.keyCode === 100) {
            document.getElementById("list-profile-list_inf_operation").click()
        }
        else if (event.keyCode === 53 || event.keyCode === 101) {
            document.getElementById("list-profile-list_inf_ks_zabolev").click()
        }
        else if (event.keyCode === 54 || event.keyCode === 102) {
            document.getElementById("list-profile-list_inf_complication").click()
        }
        else if (event.keyCode === 55 || event.keyCode === 103) {
            document.getElementById("list-profile-list_inf_work_capacity").click()
        }
        else if (event.keyCode === 56 || event.keyCode === 104) {
            document.getElementById("list-profile-list_inf_manipulation").click()
        }
        else if (event.keyCode === 57 || event.keyCode === 105) {
            document.getElementById("list-profile-list_inf_translations").click()
        }
        else if (event.keyCode === 65) {
            document.getElementById("list-profile-list_inf_post_mortem").click()
        }
        else if (event.keyCode === 66) {
            document.getElementById("list-profile-list_inf_injury").click()
        }
        else if (event.keyCode === 67) {
            document.getElementById("list-profile-list_inf_policy_passport_snills").click()
        }
        else if (event.keyCode === 68) {
            document.getElementById("list-profile-list_inf_pregnancy").click()
        }
        else if (event.keyCode === 69) {
            document.getElementById("list-profile-list_inf_disability").click()
        }
        else if (event.keyCode === 70) {
            document.getElementById("list-profile-list_inf_patient_p").click()
        }
        else if (event.keyCode === 73) {
            document.getElementById("list-profile-list_inf_onmk").click()
        }
        else if (event.keyCode === 74) {
            document.getElementById("list-profile-list_inf_onk").click()
        }
        else if (event.keyCode === 75) {
            document.getElementById("list-profile-list_inf_mo").click()
        }
    }

}

function stop_tab() {
    if (event.target.id != "aro_n" && event.target.id != "vb_a_datv" && event.target.id != "srber"
        && event.target.id != "n_ber" && event.target.id != "pria" && event.target.id != "m_prer"
        && event.target.id != "vs_bol" && event.target.id != "napr_usl" && event.target.name != "py"
        && event.target.name != "goc" && event.target.name != "pop" && event.target.name != "inf_oper"
        && event.target.name != "xosl" && event.target.name != "posl" && event.target.name != "aosl"
        && event.target.name != "pl") {
        return true
    }
}