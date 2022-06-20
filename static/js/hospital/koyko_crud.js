function Koyko_add() {
    var an_rem = document.getElementById("an_rem")
    let tbody = document.getElementById('koyko_table').querySelector('tbody')
    let tr = document.createElement('tr')
    let add_btn = document.getElementById('add_tr_koyko')
    add_btn.setAttribute('disabled', 'disabled')
    let koyko_td = ['N', 'aro', 'otd', 'prof_k', 'kod', 'naim', 'spec', 'btn']
    for (let i = 0; i < koyko_td.length; i++) {
        let td = document.createElement('td')
        td.setAttribute("name", koyko_td[i])
        if (koyko_td[i] == "btn") {

            // let btn = document.createElement("input")
            // btn.setAttribute('type', 'button')
            // btn.classList.add('btn')
            // btn.classList.add('btn-danger')
            // btn.setAttribute("name", "btn")
            // btn.value = 'Удалить'
            // btn.addEventListener("click", function () {
            //     tr.remove()
            //     add_btn.removeAttribute('disabled')
            //     app.$data.history.le_vr = []
            //     an_rem.setAttribute('style','display:none')
            // })
            // td.appendChild(btn)
            // tr.appendChild(td)


        }
        else {
            var ed = document.createElement("input")
            if (koyko_td[i] == 'N' || koyko_td[i] == 'aro' || koyko_td[i] == 'otd') {
                ed.setAttribute("style", "width:40px")
            }
            else if (koyko_td[i] == 'prof_k') {
                ed.setAttribute("style", "width:410px")
            }
            else if (koyko_td[i] == 'kod') {
                ed.setAttribute("style", "width:75px")
            }
            else {
                ed.setAttribute("style", "width:190px")
            }
            if (koyko_td[i] == 'N') {
                ed.setAttribute("name", koyko_td[i])
            }
            td.appendChild(ed)
            tr.appendChild(td)
        }
    }
    tbody.appendChild(tr)
    let obj = new Object()
    obj.N = ''
    obj.aro = ''
    obj.otd = ''
    obj.prof_k = ''
    obj.kod = ''
    obj.naim = ''
    obj.spec = ''
    obj.aro_n = ''
    obj.aro_let = ''
    obj.aro_sofa = ''
    obj.aro_ivl = ''
    app.$data.history.le_vr = obj
    Koyko_input()
    an_rem.setAttribute('style', 'display:none')
}
function Koyko_edit() {
    document.getElementById("inf_koyko").scrollLeft = 0
    let tbody = document.getElementById('koyko_table').querySelector('tbody')
    let add_btn = document.getElementById('add_tr_koyko')
    tbody.innerHTML = ""
    let le_vr = app.$data.history.le_vr
    // var an_rem = document.getElementById("an_rem")
    if (le_vr.N != undefined || le_vr.aro != undefined || le_vr.otd != undefined
        || le_vr.prof_k != undefined || le_vr.kod != undefined) {
        let tr = document.createElement("tr")

        for (let l in le_vr) {
            if (l == "aro_n" || l == "aro_let" || l == "aro_sofa" || l == "aro_ivl") {
                continue
            }
            let td = document.createElement("td")
            var ed = document.createElement("input")
            if (l == 'N') {
                ed.setAttribute("name", l)
            }
            // ed.setAttribute("name", l)
            ed.value = le_vr[l]
            if (l == 'N' || l == 'aro' || l == 'otd') {
                ed.setAttribute("style", "width:40px")
                if (l == 'aro') {
                    // console.log(le_vr[l])
                    if (le_vr[l] == null) {
                        an_rem.setAttribute('style', 'display:none')
                    }
                    else {
                        an_rem.setAttribute('style', 'border:1px solid')
                    }
                }
            }
            else if (l == 'prof_k') {
                ed.setAttribute("style", "width:410px")
            }
            else if (l == 'kod') {
                ed.setAttribute("style", "width:75px")
            }
            else {
                ed.setAttribute("style", "width:190px")
            }
            td.appendChild(ed)
            td.setAttribute("name", l)
            tr.appendChild(td)
        }


        // let td = document.createElement("td")
        // td.setAttribute("name", "btn")
        // let btn = document.createElement("input")
        // btn.setAttribute('type', 'button')
        // btn.classList.add('btn')
        // btn.classList.add('btn-danger')
        // btn.value = 'Удалить'

        // btn.addEventListener("click", function () {
        //     tr.remove()
        //     add_btn.removeAttribute('disabled')
        //     app.$data.history.le_vr = []
        //     an_rem.setAttribute('style','display:none')
        // })

        // td.appendChild(btn)
        // tr.appendChild(td)

        tbody.appendChild(tr)

        // Koyko_click_edit()
        Koyko_input()
    }
    else {
        Koyko_add()
    }
    setTimeout(() => {
        $('input[name="N"]').focus()
    }, 500)
    // document.getElementById("add_tr_koyko").removeAttribute("disabled")
}

function Koyko_input() {
    // console.log('input')
    var table = document.getElementById("koyko_table")
    var cells = table.getElementsByTagName("td")
    var prof_k = app.$data.sprav_list.V020
    var str_prof_k = ''
    for (var i = 0; i < prof_k.length; ++i) {
        str_prof_k += '<option value="' + prof_k[i].kPrname + '" />'
    }

    // var vra_kod = app.$data.sprav_list.Vra
    var str_vra_kod = ''
    // for (var i = 0; i < vra_kod.length; ++i) {
    //     str_vra_kod += '<option value="' + vra_kod[i].kod + '" />'
    // }

    var an_rem = document.getElementById("an_rem")
    for (let i = 0; i < cells.length; i++) {
        if ((cells[i].getAttribute("name") != "naim") && (cells[i].getAttribute("name") != "spec") && (cells[i].getAttribute("name") != "btn")) {
            let input = cells[i].childNodes[0]
            input.setAttribute('name', cells[i].getAttribute("name"))
            if (cells[i].getAttribute('name') == 'prof_k') {
                let data = document.createElement("datalist")
                data.setAttribute('id', 'prof_k')
                data.innerHTML = str_prof_k
                input.setAttribute('list', 'prof_k')
                cells[i].append(data)
            }
            // if (cells[i].getAttribute('name') == 'kod') {
            //     let kod_vra = app.$data.sprav_list.Vra
            //     let str_vra = ''
            //     for (let k = 0; k < kod_vra.length; k++) {
            //         str_vra += '<option value="' + kod_vra[k].kod + '" />'
            //     }
            //     console.log(str_vra)
            //     // input.setAttribute('list', cells[i].getAttribute("name"))
            //     // let data_lis = document.createElement("datalist")
            //     // data_lis.setAttribute('id', cells[i].getAttribute("name"))
            //     // data_lis.innerHTML = str_vra
            //     // input.appendChild(data_lis)
            //     // data_lis.setAttribute('list','kod_le')
            //     // // console.log(data_lis)
            // }

            if (cells[i].getAttribute('name') != 'aro' && cells[i].getAttribute('name') != 'kod') {
                input.addEventListener('change', function () {
                    Koyko_update()
                })
            }
            else if (cells[i].getAttribute('name') == 'aro') {
                input.addEventListener('change', function () {
                    Koyko_update()
                    if (input.value != '0' && input.value != '') {
                        an_rem.setAttribute('style', 'border:1px solid')
                    }
                    else {
                        an_rem.setAttribute('style', 'display:none')
                        app.$data.history.gwf = ''
                        app.$data.history.u_gwf = ''
                        app.$data.history.sofa = ''
                        app.$data.history.iwl = ''
                    }
                })


            }

            else {
                let data_list = document.createElement("datalist")
                data_list.setAttribute('id', 'kod_le')
                // data.innerHTML = str_vra_kod
                input.setAttribute('list', 'kod_le')
                let kod_vra = app.$data.sprav_list.Vra
                let str_vra = ''
                for (let k = 0; k < kod_vra.length; k++) {
                    str_vra += '<option value="' + kod_vra[k].kod + '" />'
                }
                data_list.innerHTML = str_vra

                cells[i].append(data_list)
                input.addEventListener('focus', function () {
                    document.getElementById("inf_koyko").scrollLeft = 300
                })


                // input.addEventListener("input", function () {
                //     let query = `
                //     query{
                //         VraList(vra:"${input.value}"){
                //             kod
                //         }
                //     }`
                //     fetch('graph_hospital/', {
                //         method: 'post',
                //         headers: {
                //             'Content-Type': 'application/json',
                //         },
                //         body: JSON.stringify({ query })
                //     })
                //         .then(response => response.json())
                //         .then(data => {
                //             str_vra_kod = ""
                //             for (vra of data.data.VraList) {
                //                 str_vra_kod += '<option value="' + vra.kod + '" />'
                //                 // console.log(str_vra)
                //                 data_list.innerHTML = str_vra_kod
                //             }

                //         })
                //         .catch((e) => {
                //             //   console.log(e)
                //         })
                // })


                input.addEventListener('change', function () {
                    let query = `
                          query{
                              VraName(kod:"${input.value}"){
                                naim
                                kodSpec
                                nSpec
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
                            for (let i = 0; i < cells.length; i++) {
                                if (cells[i].getAttribute("name") == "naim") {
                                    cells[i].childNodes[0].value = data.data.VraName[0].naim
                                    // console.log(data.data.VraName[0].nSpec)
                                    Koyko_update()
                                }
                                else if (cells[i].getAttribute("name") == "spec") {
                                    cells[i].childNodes[0].value = data.data.VraName[0].nSpec
                                    Koyko_update()
                                }
                            }
                            // let query = `
                            //   query{
                            //       V021Name(spec:"${data.data.VraName[0].kodSpec}"){
                            //         specname
                            //       }
                            //   }`
                            // fetch('graph_hospital/', {
                            //       method: 'post',
                            //       headers: {
                            //         'Content-Type': 'application/json',
                            //       },
                            //       body: JSON.stringify({query})
                            //     })
                            //     .then(response => response.json())
                            //     .then(data => {
                            //         for (let i = 0; i < cells.length; i++) {
                            //             if (cells[i].getAttribute("name") == "spec") {
                            //                 cells[i].childNodes[0].value = data.data.V021Name[0].specname
                            //                 Koyko_update()
                            //             }
                            //         }
                            //     })
                            //     .catch((e) => {
                            //     //   console.log(e)
                            //     })
                        })
                        .catch((e) => {
                            //   console.log(e)
                        })
                    Koyko_update()
                })
            }
        }



    }




}

function Koyko_update() {
    var td_cells = document.getElementById("koyko_table").querySelector("tbody").querySelector("tr").cells
    let obj = new Object()
    obj.N = td_cells[0].childNodes[0].value
    obj.aro = td_cells[1].childNodes[0].value
    obj.otd = td_cells[2].childNodes[0].value
    obj.prof_k = td_cells[3].childNodes[0].value
    obj.kod = td_cells[4].childNodes[0].value
    obj.naim = td_cells[5].childNodes[0].value
    obj.spec = td_cells[6].childNodes[0].value
    obj.aro_n = app.$data.history.le_vr.aro_n
    obj.aro_let = app.$data.history.le_vr.aro_let
    obj.aro_sofa = app.$data.history.le_vr.aro_sofa
    obj.aro_ivl = app.$data.history.le_vr.aro_ivl
    app.$data.history.le_vr = obj

}
