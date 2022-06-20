function Oper_add() {
    let tbody = document.getElementById("operation_table").querySelector("tbody")
    let count = tbody.childNodes

    if (count.length == 0) {
        var n = 0
    }
    else {
        var n = count.length
    }
    let pr = app.$data.sprav_list.PROsob
    let op_l = ['dato', 'tm_o', 'py', 'kod_op', 'kod_op_name', 'goc', 'kodx', 'kodx_naim', 'pop', 'pr_osob', 'k_mm', 'kodxa', 'kodxa1', 'obz', 'obz_2', 'kodan', 'btn']
    let tr = document.createElement("tr")
    tr.setAttribute("n", n)
    for (o in op_l) {
        let td = document.createElement("td")
        td.setAttribute("name", op_l[o])
        if (op_l[o] == "py") {
            let select = document.createElement("select")
            select.setAttribute("n", n)
            select.setAttribute("name", "py")
            select.classList.add('custom-select')
            select.classList.add('text-center')
            let py = [1, 2]
            for (let i = 0; i < py.length; i++) {
                let option = document.createElement("option")
                option.innerText = py[i]
                select.appendChild(option)
                select.value = ''
            }
            td.appendChild(select)
            td.setAttribute("name", op_l[o])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }

        else if (op_l[o] == "goc") {
            let select = document.createElement("select")
            select.setAttribute("n", n)
            select.setAttribute("name", op_l[o])
            select.classList.add('custom-select')
            select.classList.add('text-center')
            let goc = ['1', '2']
            for (let i = 0; i < goc.length; i++) {
                let option = document.createElement("option")
                option.innerText = goc[i]
                select.appendChild(option)
            }
            select.value = ''
            td.appendChild(select)
            td.setAttribute("name", op_l[o])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (op_l[o] == "pop") {
            let select = document.createElement("select")
            select.setAttribute("n", n)
            select.setAttribute("name", op_l[o])
            select.classList.add('custom-select')
            select.classList.add('text-center')
            let pop = ['Да', 'Нет', 'Неизвестно']
            for (let p of pop) {
                let option = document.createElement("option")
                option.innerText = p
                select.appendChild(option)
            }
            select.value = ''
            td.appendChild(select)
            td.setAttribute("name", op_l[o])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (op_l[o] == "pr_osob") {


            // let select = document.createElement("select")
            // select.setAttribute("n", n)
            // select.setAttribute("name", op_l[o])
            // select.classList.add('form-control')
            // select.classList.add('text-center')
            // select.setAttribute('multiple', '')
            // select.setAttribute('style', 'width: 288px')
            // for (let p = 0; p < pr.length; p++) {
            //     let option = document.createElement("option")
            //     option.value = pr[p].kod
            //     option.innerText =  pr[p].kod
            //     select.appendChild(option)
            // }

            // td.appendChild(select)
            let div = document.createElement("div")
            div.setAttribute("n", n)
            div.setAttribute("name", op_l[o])
            div.style="width:220px"
            
            
/* width: 1443px;
overflow: scroll; */


            // let div_2 = document.createElement("div")
            // div_2.setAttribute("class", "form-check")
            // let input = document.createElement("input")
            // input.setAttribute("class", "form-check-input")
            // input.setAttribute("type", "checkbox")
            // input.setAttribute("value", "")
            // input.setAttribute("id", "")
            // input.setAttribute("n", n)
            // input.setAttribute("nn", 0)
            // input.setAttribute("name", "pr_osob")
            // let label = document.createElement("label")
            // label.setAttribute("class", "form-check-label")
            // label.innerHTML = ""
            // div_2.appendChild(input)
            // div_2.appendChild(label)
            // div.appendChild(div_2)
            // let div1 = document.createElement("div")
            // let div2 = document.createElement("div")
            // let div3 = document.createElement("div")
            // div1.setAttribute("class", "form-check form-check-inline")
            // div2.setAttribute("class", "form-check form-check-inline")
            // div3.setAttribute("class", "form-check form-check-inline")

            for (let p = 0; p < pr.length; p++) {
                let div_3 = document.createElement("div")
                div_3.setAttribute("class", "form-check form-check-inline")
                let input = document.createElement("input")
                input.setAttribute("class", "form-check-input")
                input.setAttribute("type", "checkbox")
                input.setAttribute("value", pr[p].kod)
                input.setAttribute("id", pr[p].kod)
                input.setAttribute("n", n)
                input.setAttribute("nn", p)
                input.setAttribute("name", "pr_osob")
                let label = document.createElement("label")
                label.setAttribute("class", "form-check-label")
                label.innerHTML = pr[p].kod
                // div_3.setAttribute("style","padding:50px")
                div_3.appendChild(input)
                div_3.appendChild(label)
                div.appendChild(div_3)
                // if (p <= 4){
                //     div1.appendChild(div_3)
                // }
                // else if (4 < p <=8){
                //     div2.appendChild(div_3)
                // }
                // else{
                //     div3.appendChild(div_3)
                // }
            }
            // div.appendChild(div1)
            // div.appendChild(div2)
            // div.appendChild(div3)
            td.appendChild(div)




            td.setAttribute("name", op_l[o])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (op_l[o] == "btn") {
            // td.setAttribute("name", "btn")
            // let btn = document.createElement("input")
            // btn.setAttribute('type', 'button')
            // btn.classList.add('btn')
            // btn.classList.add('btn-danger')
            // btn.value = 'Удалить'
            // btn.addEventListener("click", function () {
            //     tr.remove()
            //     Oper_delete(td)
            // })
            // td.appendChild(btn)
            // tr.appendChild(td)
        }
        else {

            var ed = document.createElement("input")
            ed.setAttribute("n", n)
            ed.setAttribute("name", op_l[o])
            // ed.value = op_l[o]
            if (op_l[o] == 'dato') {
                ed.setAttribute("style", "width:100px")
                ed.setAttribute("name", op_l[o])
            }
            else if (op_l[o] == 'tm_o') {
                ed.setAttribute("style", "width:60px")
            }
            else if (op_l[o] == 'py') {
                ed.setAttribute("style", "width:50px")
            }
            else if (op_l[o] == 'kod_op') {
                ed.setAttribute("style", "width:150px")
            }
            else if (op_l[o] == 'kod_op_name') {
                ed.setAttribute("style", "width:310px")
            }
            else if (op_l[o] == 'goc') {
                ed.setAttribute("style", "width:50px")
            }
            else if (op_l[o] == 'kodx') {
                ed.setAttribute("style", "width:100px")
            }
            else if (op_l[o] == 'kodx_naim') {
                ed.setAttribute("style", "width:140px")
            }
            else if (op_l[o] == 'k_mm') {
                ed.setAttribute("style", "width:60px")
            }
            else if (op_l[o] == 'kodxa') {
                ed.setAttribute("style", "width:100px")
            }
            else if (op_l[o] == 'kodxa1') {
                ed.setAttribute("style", "width:100px")
            }
            else if (op_l[o] == 'obz' || op_l[o] == 'obz_2') {
                ed.setAttribute("style", "width:80px")
            }
            else if (op_l[o] == 'kodan') {
                ed.setAttribute("style", "width:100px")
            }

            td.appendChild(ed)


            td.setAttribute("name", op_l[o])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }

    }
    tbody.appendChild(tr)
    obj = {}
    for (let t = 0; t < tr.childNodes.length; t++) {
        let td = tr.childNodes[t]
        if (td.getAttribute("name") != "btn") {
            if (td.getAttribute("name") != "pr_osob") {
                obj[td.getAttribute("name")] = ''
            }
            else {
                obj[td.getAttribute("name")] = []
            }
        }
    }
    app.$data.history.oper.push(obj)
    Oper_input()
    let add_btn = document.getElementById("add_tr_koyko")
    add_btn.setAttribute("disabled", "disabled")
}

function Oper_edit() {
    document.getElementById("inf_operation").scrollLeft = 0
    let tbody = document.getElementById("operation_table").querySelector("tbody")
    tbody.innerHTML = ""
    let v_oper = app.$data.history.oper
    let pr = app.$data.sprav_list.PROsob
    var n = 0
    if (v_oper.length > 0) {
        for (let opers in v_oper) {
            let oper = v_oper[opers]
            let tr = document.createElement("tr")
            tr.setAttribute("n", n)
            for (o in oper) {
                let td = document.createElement("td")
                if (o == "py") {
                    let select = document.createElement("select")
                    select.classList.add('custom-select')
                    select.classList.add('text-center')
                    select.setAttribute("name", "py")
                    let py = [1, 2]
                    for (let i = 0; i < py.length; i++) {
                        let option = document.createElement("option")
                        option.innerText = py[i]
                        select.appendChild(option)
                    }
                    select.value = oper[o]
                    select.setAttribute("n", n)
                    select.setAttribute("name", o)
                    td.appendChild(select)
                    td.setAttribute("name", o)
                    td.setAttribute("tr", n)
                    tr.appendChild(td)
                }
                else if (o == "goc") {
                    let select = document.createElement("select")
                    select.setAttribute("n", n)
                    select.setAttribute("name", o)
                    select.classList.add('custom-select')
                    select.classList.add('text-center')
                    let goc = ['1', '2']
                    for (let i = 0; i < goc.length; i++) {
                        let option = document.createElement("option")
                        option.innerText = goc[i]
                        select.appendChild(option)
                    }
                    select.value = oper[o]
                    select.setAttribute("n", n)
                    td.appendChild(select)
                    td.setAttribute("name", o)
                    td.setAttribute("tr", n)
                    tr.appendChild(td)
                }
                else if (o == "pop") {
                    let select = document.createElement("select")
                    select.setAttribute("n", n)
                    select.setAttribute("name", o)
                    select.classList.add('custom-select')
                    select.classList.add('text-center')
                    let pop = ['Да', 'Нет', 'Неизвестно']
                    for (let p of pop) {
                        let option = document.createElement("option")
                        option.innerText = p
                        select.appendChild(option)
                    }
                    select.value = oper[o]
                    if (select.value == 'Да') {
                        $("#oper_osn").val(oper['kod_op'])
                    }

                    td.appendChild(select)
                    td.setAttribute("name", o)
                    td.setAttribute("tr", n)
                    tr.appendChild(td)
                }
                else if (o == "pr_osob") {
                    // let select = document.createElement("select")
                    // select.setAttribute("n", n)
                    // select.setAttribute("name", o)
                    // select.classList.add('form-control')
                    // select.classList.add('text-center')
                    // select.setAttribute('multiple', '')
                    // select.setAttribute('style', 'width: 288px')
                    // for (let p = 0; p < pr.length; p++) {
                    //     let option = document.createElement("option")
                    //     option.value = pr[p].kod
                    //     option.innerText = pr[p].kod
                    //     select.appendChild(option)
                    // }
                    // options = Array.from(select.childNodes)
                    // td.appendChild(select)

                    // oper[o].forEach(function (v) {
                    //     options.find(c => c.value == v).selected = true;

                    // });

                    let div = document.createElement("div")
                    div.setAttribute("n", n)
                    div.setAttribute("name", o)
                    div.style="width:220px"

                    for (let p = 0; p < pr.length; p++) {
                        let div_3 = document.createElement("div")
                        div_3.setAttribute("class", "form-check form-check-inline")
                        let input = document.createElement("input")
                        input.setAttribute("class", "form-check-input")
                        input.setAttribute("type", "checkbox")
                        input.setAttribute("value", pr[p].kod)
                        input.setAttribute("id", pr[p].kod)
                        input.setAttribute("n", n)
                        input.setAttribute("nn", p)
                        input.setAttribute("name", "pr_osob")
                        oper[o].forEach(function (v) {
                            if (v == pr[p].kod){
                                input.checked = true
                            }
                        });
                        let label = document.createElement("label")
                        label.setAttribute("class", "form-check-label")
                        label.innerHTML = pr[p].kod
                        div_3.appendChild(input)
                        div_3.appendChild(label)
                        div.appendChild(div_3)
                    }

                    td.appendChild(div)

                    td.setAttribute("name", o)
                    td.setAttribute("tr", n)
                    tr.appendChild(td)
                }
                else {
                    var ed = document.createElement("input")
                    ed.setAttribute("n", n)
                    ed.setAttribute("name", o)
                    ed.value = oper[o]
                    if (o == 'dato') {
                        ed.setAttribute("style", "width:100px")
                        ed.setAttribute("name", o)
                    }
                    else if (o == 'tm_o') {
                        ed.setAttribute("style", "width:60px")
                    }
                    else if (o == 'py') {
                        ed.setAttribute("style", "width:50px")
                    }
                    else if (o == 'kod_op') {
                        ed.setAttribute("style", "width:150px")
                    }
                    else if (o == 'kod_op_name') {
                        ed.setAttribute("style", "width:310px")
                    }
                    else if (o == 'goc') {
                        ed.setAttribute("style", "width:50px")
                    }
                    else if (o == 'kodx') {
                        ed.setAttribute("style", "width:100px")
                    }
                    else if (o == 'kodx_naim') {
                        ed.setAttribute("style", "width:140px")
                    }
                    else if (o == 'k_mm') {
                        ed.setAttribute("style", "width:60px")
                    }
                    else if (o == 'kodxa') {
                        ed.setAttribute("style", "width:100px")
                    }
                    else if (o == 'kodxa1') {
                        ed.setAttribute("style", "width:100px")
                    }
                    else if (o == 'obz' || o == 'obz_2') {
                        ed.setAttribute("style", "width:80px")
                    }
                    else if (o == 'kodan') {
                        ed.setAttribute("style", "width:100px")
                    }

                    td.appendChild(ed)
                    td.setAttribute("name", o)
                    td.setAttribute("tr", n)
                    tr.appendChild(td)
                }

            }

            tbody.appendChild(tr)
            if (tr.childNodes[8].childNodes[0].value == "Да"){
                tr.style = "background:#d1e7dd"
            }
                                // let tbody = document.getElementById("operation_table").querySelector("tbody")
                    // let op_tr =  tbody.querySelector(`tr[n='${n}']`)
                    // console.log(op_tr)
            n += 1
        }
        Oper_input()
    }
    else {
        // let add_btn = document.getElementById("add_tr_koyko")
        // add_btn.removeAttribute("disabled")
        // Oper_add()
    }

}

function Oper_input() {
    let kod = app.$data.sprav_list.V001
    let str_kod_v001 = ''
    for (let k = 0; k < kod.length; k++) {
        str_kod_v001 += '<option value="' + kod[k].kod + '" />'
    }

    let kod_vra = app.$data.sprav_list.Vra
    let str_vra = ''
    for (let k = 0; k < kod_vra.length; k++) {
        str_vra += '<option value="' + kod_vra[k].kod + '" />'
    }
    let kod_obez = app.$data.sprav_list.anesthesia
    let str_obez = ''
    for (let k = 0; k < kod_obez.length; k++) {
        str_obez += '<option value="' + kod_obez[k].kod + '" />'
    }
    var table = document.getElementById("operation_table")
    var cells = table.getElementsByTagName("td")

    for (let i = 0; i < cells.length; i++) {
        if ((cells[i].getAttribute("name") == "dato") || (cells[i].getAttribute("name") == "tm_o") || (cells[i].getAttribute("name") == "kod_op")
            || (cells[i].getAttribute("name") == "kodx") || (cells[i].getAttribute("name") == "kodxa")
            || (cells[i].getAttribute("name") == "kodxa1") || (cells[i].getAttribute("name") == "obz") || (cells[i].getAttribute("name") == "obz_2") || (cells[i].getAttribute("name") == "kodan")) {

            let input = cells[i].childNodes[0]
            if (cells[i].getAttribute("name") == "dato") {
                input.setAttribute("maxlength", 8)
                input.addEventListener("input", function () {
                    var n = input.value.replace(/[^0-9]/g, '').split('')
                    if (n.length > 2) n.splice(2, 0, '-')
                    if (n.length > 4) n.splice(5, 0, '-')
                    input.value = n.join('')
                })
                input.addEventListener("change", function () {
                    Oper_update(cells[i])
                })
            }
            else if (cells[i].getAttribute("name") == "tm_o") {
                input.setAttribute("maxlength", 5)
                input.addEventListener("input", function () {
                    var n = input.value.replace(/[^0-9]/g, '').split('')
                    if (n.length > 2) n.splice(2, 0, ':')
                    input.value = n.join('')
                })
                input.addEventListener("change", function () {
                    Oper_update(cells[i])
                })
            }
            else if (cells[i].getAttribute("name") == "kod_op") {

                input.addEventListener('focus', function () {
                    // document.getElementById("inf_operation").scrollLeft = 500
                })
                input.setAttribute('list', cells[i].getAttribute("name"))
                let data_list = document.createElement("datalist")
                data_list.setAttribute('id', cells[i].getAttribute("name"))
                data_list.innerHTML = str_kod_v001
                input.appendChild(data_list)
                input.addEventListener("input", function () {
                    input.value = input.value.replace(",", ".")
                    // data.innerHTML = str_kod
                    // str_kod_v001 = ""
                    // let query = `
                    // query{
                    //     V001List(kod:"${input.value.replace(",",".")}"){
                    //         kod
                    //     }
                    // }`
                    // fetch('graph_hospital/', {
                    //     method: 'post',
                    //     headers: {
                    //         'Content-Type': 'application/json',
                    //     },
                    //     body: JSON.stringify({ query })
                    // })
                    //     .then(response => response.json())
                    //     .then(data => {
                    //         // str_kod_v001 = ""
                    //         // console.log(data.data.V001List)
                    //         for (kod of data.data.V001List) {
                    //             str_kod_v001 += '<option value="' + kod.kod + '" />'
                    //             // console.log(str_vra)
                    //             data_list.innerHTML = str_kod_v001
                    //         }

                    //     })
                    //     .catch((e) => {
                    //         //   console.log(e)
                    //     })

                })
                input.addEventListener("change", function () {
                    let query = `
                          query{
                              V001Name(kod:"${input.value}"){
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
                            var tr_list = document.getElementById("operation_table").querySelector("tbody").querySelectorAll("tr")
                            var tr = tr_list[cells[i].getAttribute("tr")]
                            var naim = tr.childNodes[4]
                            naim.childNodes[0].value = data.data.V001Name[0].naim
                            Oper_update(tr.childNodes[3])
                            Oper_update(tr.childNodes[4])
                        })
                        .catch((e) => {
                            //   console.log(e)
                        })

                })
            }
            else if (cells[i].getAttribute("name") == "goc") {
                let select = cells[i].childNodes[0]
                select.addEventListener('focus', function () {
                    // document.getElementById("inf_operation").scrollLeft = 800
                })
            }
            else if ((cells[i].getAttribute('name') == "kodx") || (cells[i].getAttribute('name') == "kodxa")
                || (cells[i].getAttribute('name') == "kodxa1") || (cells[i].getAttribute('name') == "kodan")) {
                input.setAttribute('list', cells[i].getAttribute("name"))
                let data_lis = document.createElement("datalist")
                data_lis.setAttribute('id', cells[i].getAttribute("name"))
                data_lis.innerHTML = str_vra
                input.appendChild(data_lis)

                input.addEventListener("input", function () {


                    // data.innerHTML = '<option value="' + '1234' + '" />'
                    // console.log(input.value)
                    // input.value.replace(".",",")
                    // let query = `
                    // query{
                    //     VraList(vra:"${input.value}"){
                    //         kod
                    //     }
                    // }`
                    // fetch('graph_hospital/', {
                    //     method: 'post',
                    //     headers: {
                    //         'Content-Type': 'application/json',
                    //     },
                    //     body: JSON.stringify({ query })
                    // })
                    //     .then(response => response.json())
                    //     .then(data => {
                    //         str_vra = ""
                    //         for (vra of data.data.VraList) {
                    //             str_vra += '<option value="' + vra.kod + '" />'
                    //             // console.log(str_vra)
                    //             data_lis.innerHTML = str_vra
                    //         }

                    //     })
                    //     .catch((e) => {
                    //         //   console.log(e)
                    //     })
                })

                if (cells[i].getAttribute('name') == "kodx") {
                    input.addEventListener('focus', function () {
                        // document.getElementById("inf_operation").scrollLeft = 450
                    })

                    // input.addEventListener('oninput',function(){
                    //     console.log('asdw')
                    // })

                    input.addEventListener('change', function () {
                        let query = `
                          query{
                              VraName(kod:"${input.value}"){
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
                                var tr_list = document.getElementById("operation_table").querySelector("tbody").querySelectorAll("tr")
                                var tr = tr_list[cells[i].getAttribute("tr")]
                                var naim = tr.childNodes[7]
                                naim.childNodes[0].value = data.data.VraName[0].naim
                                Oper_update(tr.childNodes[6])
                                Oper_update(tr.childNodes[7])
                            })
                            .catch((e) => {
                                //   console.log(e)
                            })
                    })
                }

                else {
                    input.addEventListener("change", function () {
                        Oper_update(cells[i])
                    })
                    if (cells[i].getAttribute('name') == "kodxa") {
                        input.addEventListener('focus', function () {
                            // document.getElementById("inf_operation").scrollLeft = 1150
                        })
                    }
                }
            }

            else if (cells[i].getAttribute('name') == "obz" || cells[i].getAttribute('name') == "obz_2") {
                input.addEventListener("input", function () {
                    input.setAttribute('list', cells[i].getAttribute("name"))
                    let data = document.createElement("datalist")
                    data.setAttribute('id', cells[i].getAttribute("name"))
                    data.innerHTML = str_obez
                    input.appendChild(data)
                })

                input.addEventListener("change", function () {
                    Oper_update(cells[i])
                })
            }
        }
        else if (cells[i].getAttribute("name") == "pop") {

            let select = cells[i].childNodes[0]
            select.addEventListener('focus', function () {
                // document.getElementById("inf_operation").scrollLeft = 1200
            })
            select.addEventListener("change", function () {
                Oper_update(cells[i])
                let tbody = document.getElementById("operation_table").querySelector("tbody")
                let op_tr =  tbody.querySelector(`tr[n='${cells[i].getAttribute("tr")}']`)
                if (cells[i].childNodes[0].value == 'Да') {
                    $("#oper_osn").val(cells[3].childNodes[0].value)
                    op_tr.style = "background:#d1e7dd"
                }
                else{
                    op_tr.style = ""
                }

            })
        }

        else {
            let select = cells[i].childNodes[0]
            select.addEventListener("change", function () {
                Oper_update(cells[i])
            })
        }

    }
}

function Oper_delete(td) {
    let v_oper = app.$data.history.oper
    let oper = []

    for (let c = 0; c < v_oper.length; c++) {
        if (c != td.getAttribute("tr")) {
            oper.push(v_oper[c])
        }
    }
    app.$data.history.oper = oper
    Oper_edit()
    Oper_input()
}
function Oper_update(td) {
    var v_oper = app.$data.history.oper
    if (td.getAttribute("name") != "pr_osob") {
        v_oper[td.getAttribute("tr")][td.getAttribute("name")] = td.childNodes[0].value
    }
    else {
        console.log(app.$data.history.oper)
        let checkboxs = td.childNodes[0].querySelectorAll("input")
        let active = []
        for (c in checkboxs) {
            try {
                if (checkboxs[c].hasAttribute("id")) {
                    if (checkboxs[c].value != ""){
                        if (checkboxs[c].checked){
                            active.push(checkboxs[c].value)
                        }
                        // active.push(c.value)
                    }
                    else{
                        active = []
                    }
                }
            }
            catch {

            }
        }
        v_oper[td.getAttribute("tr")][td.getAttribute("name")] = active
        // let select_active = td.childNodes[0].selectedOptions
        // console.log(app.$data.history.oper)
        // let active = []
        // for (let a of select_active) {
        //     active.push(a.value)
        // }
        // v_oper[td.getAttribute("tr")][td.getAttribute("name")] = active
    }

}
