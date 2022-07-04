var spec = null
var prof = null
function start_prot() {
    prot_clear()

    // let SPEC = function () {
    // let query = `
    //           query{
    //               VraName(kod:"${get_spec()}"){
    //                 v021
    //               }
    //           }`
    // let rez = graphql(query)
    // }

    // console.log(SPEC)
    spec = SPEC()
    prof = PROF()

    prot_1()
    prot_2()
    // prot_3()
    // prot_4() Неактуально
    prot_5()


    // prot_6()
    prot_7()
    prot_8()
    prot_9()
    prot_10()
    prot_11()
    prot_12()
    prot_13()
    prot_14()
    prot_15()
    prot_16()
    prot_17()
    prot_18()
    prot_19()
    prot_20()
    prot_21()
    prot_22()
    prot_23()
    prot_24()
    prot_25()
//    prot_26()
    prot_27()
}

function SPEC() {
    let query = `
              query{
                  VraName(kod:"${get_spec()}"){
                    v021
                  }
              }`
    let rez = graphql(query)
    rez.then(value => {
        if (value.VraName.length != 0) {
            return value.VraName[0].v021
        }
        return null
    })
}

function PROF() {
    let query = `
              query{
                  VraName(kod:"${get_spec()}"){
                    v002
                  }
              }`
    let rez = graphql(query)
    rez.then(value => {
        if (value.VraName.length != 0) {
            return value.VraName[0].v002
        }
        return null
    })
}

//Взаимное несоответствие исхода заболевания, результата обращения
function prot_1() {
    try {
        if ($("#icx").val() != '' && $("#rslt").val() != '') {
            var rslt_l = ['102', '103', '104', '105', '106', '109', '108', '107', '110']
            if (rslt_l.indexOf($("#rslt").val().match(/\d{3}/)[0]) != -1) {
                if ($("#icx").val().match(/\d{3}/)[0] == 101) {
                    add_prot('Взаимное несоответствие исхода заболевания, результата обращения')
                }
            }
        }
    }
    catch {

    }
}

//Несоответствие результата обращения и исхода заболевания (летальность)
function prot_2() {
    try {
        if ($("#icx").val() != '' && $("#rslt").val() != '') {
            var rslt_l = ['105', '106']
            if (rslt_l.indexOf($("#rslt").val().match(/\d{3}/)[0]) != -1) {
                if ($("#icx").val().match(/\d{3}/)[0] == 104) {
                    add_prot('Несоответствие результата обращения и исхода заболевания (летальность)')
                }
            }
        }
    } catch {

    }
}



//Значение KD не должно быть равно 0 и не должно превышать длительность лечения в календарных днях (определяется на основании дат DATE_1 и DATE_2).
function prot_3() {

    var date_1 = $("#datp").val()
    var date_2 = $("#datv").val()
    var d_l_1 = date_1.split("-")
    var d_l_2 = date_2.split("-")
    var d1 = new Date(d_l_1[2], d_l_1[1], d_l_1[0])
    var d2 = new Date(d_l_2[2], d_l_2[1], d_l_2[0])
    var d_n = diffDates(d2, d1)
    var koyko_table = document.getElementById("koyko_table").querySelector("tbody").querySelectorAll("td")
    var aro = koyko_table[1]
    if (aro != undefined) {
        if (aro.childNodes[0].value != '' && Number(aro.childNodes[0].value) == 0) {
            add_prot('Значение всего в койко-дни не должно быть равно 0')
        }
        else if (Number(aro.childNodes[0].value) > d_n) {
            add_prot('Значение всего в койко-дни не должно превышать длительность лечения в календарных днях')
        }
    }

}

//RSLT должен быть >100 и <200
function prot_4() {
    try {
        if ($("#rslt").val() != '') {
            if (100 < $("#icx").val().match(/\d{3}/)[0] < 200) {
                add_prot('RSLT должен быть >100 и <200')
            }
        }
    }
    catch { }
}


//Несоответствие специальности виду оказываемой медицинской помощи
function prot_5() {
    if (($("#vds").val() == "OМС(КСГ базов.программа)") || ($("#vds").val() == "OMC(КСГ сверхбаз.прогр-ма")) {
        if (spec != null) {
            var prvs_l = ['42', '67', '82', '83', '1', '7', '14', '16', '29', '30', '34', '42', '51', '52', '53',
                '54', '63', '64', '67', '73', '74', '82', '83', '85', '86', '88', '96', '97', '98', '99', '234', '280']
            if (prvs_l.indexOf(spec) != -1) {
                add_prot('Несоответствие специальности виду оказываемой медицинской помощи')
            }
        }
    }
}

//Возраст пациента на дату начала законченного случая должен быть  14 лет или более
function prot_6() {
    if ($("#udl").val() != '') {
        let query = `
              query{
                  F011Doc(name:"${$("#udl").val()}"){
                    idDoc
                  }
              }`
        let rez = graphql(query)
        rez.then(value => {
            var doctype_l = [1, 4, 5, 6, 7, 8, 14, 16, 17, 26, 29]
            if (doctype_l.indexOf(value.F011Doc[0].idDoc) != -1) {
                if ((get_age() / 365) < 14) {
                    add_prot('Возраст пациента на дату начала законченного случая должен быть  14 лет или более')
                }
            }
        })
    }
}



//Дата окончания лечения больше даты смерти пациента
//Дата начала лечения больше даты смерти пациента
function prot_7() {
    if ($("#wskr_date").val() != "") {
        var date_1 = $("#datp").val()
        var date_2 = $("#datv").val()
        var date_3 = $("#wskr_date").val()
        var d_l_1 = date_1.split("-")
        var d_l_2 = date_2.split("-")
        var d_l_3 = date_3.split("-")
        var d1 = new Date(d_l_1[2], d_l_1[1], d_l_1[0])
        var d2 = new Date(d_l_2[2], d_l_2[1], d_l_2[0])
        var d3 = new Date(d_l_3[2], d_l_3[1], d_l_3[0])

        if (d1 > d3) {
            add_prot('Дата начала лечения больше даты смерти пациента')
        }
        if (d2 > d3) {
            add_prot('Дата окончания лечения больше даты смерти пациента')
        }
    }

}

//Специальность врача не соответствует возрасту пациента
function prot_8() {
    let spec_l = [19, 18, 68, 21, 49, 22, 20]
    if (spec != null) {
        if (spec_l.indexOf(Number(spec)) != -1) {
            if ((get_age() / 365) > 18) {
                add_prot('Специальность врача не соответствует возрасту пациента должно применяться только для пациента младше 18')
            }
        }
    }
}

//Значение специальности врача «Акушерство и гинекология» должно применяться только для пола пациента W=2
function prot_9() {

    if (($("#pol").val() != '') && ($("#pol").val() == 'Мужской')) {
        if (spec != null) {
            if (spec == '2') {
                add_prot('Значение специальности врача «Акушерство и гинекология» должно применяться только для пола пациента Женский')
            }
        }
    }

}


//Значение специальности врача «Неонатология» должно применяться только для пациента младше 1 года.
function prot_10() {
    if (spec != null) {
        if (spec == '37') {
            if ((get_age() / 365) > 1) {
                add_prot('Значение специальности врача «Неонатология» должно применяться только для пациента младше 1 года.')
            }
        }
    }

}

function prot_11() {
    if (spec != null) {
        let spec_l = [92, 41, 84, 25]
        if (spec_l.indexOf(Number(spec)) != -1) {
            if ((get_age() / 365) < 18) {
                add_prot('Специальности врача из множества {Кардиология, Онкология, Урология, Эндокринология} должно применяться только для пациентов  18 лет и старше')
            }
        }
    }
}

//Значение специальности врача «Терапия» может применяться только для пациентов  от 15 лет и старше.Возраст пациента вычисляется на дату начала случая
function prot_12() {
    if (spec != null) {
        if (spec == '76') {
            if ((get_age() / 365) < 15) {
                add_prot('Значение специальности врача «Терапия» может применяться только для пациентов  от 15 лет и старше')
            }
        }
    }
}

//Значение специальности врача «Гериатрия» может применяться только для пациентов  60 лет и старше
function prot_13() {
    if (spec != null) {
        if (spec == '11') {
            if ((get_age() / 365) < 60) {
                add_prot('Значение специальности врача «Гериатрия» может применяться только для пациентов  60 лет и старше')
            }
        }
    }

}

//Значение специальности врача из множества {Детская кардиология, Детская онкология, Детская урология-андрология, Детская хирургия, Детская эндокринология, Педиатрия, Стоматология детская} должно применяться только для пациента младше 18 лет. Возраст пациента вычисляется на дату начала случая
function prot_14() {
    if (spec != null) {
        let spec_l = [19, 18, 68, 21, 49, 22, 20]
        if (spec_l.indexOf(Number(spec)) != -1) {
            if ((get_age() / 365) > 18) {
                add_prot('Специальность врача не соответствует возрасту пациента должно применяться только для пациента младше 18 лет.')
            }
        }
    }

}

//Профиль медицинской помощи возраст пациента должен быть меньше 18 лет
function prot_15() {
    if (prof != null) {
        let prof_l = [17, 18, 19, 20, 21, 68, 86]
        if (prof_l.indexOf(Number(prof)) != -1) {
            if ((get_age() / 365) > 18) {
                add_prot('Профиль медицинской помощи не соответствует возрасту пациента возраст пациента должен быть меньше 18 лет')
            }
        }
    }
}


//Профиль медицинской помощи Пол пациента должен быть женским
function prot_16() {
    if (prof != null) {
        let prof_l = [3, 136, 137, 184]
        if (prof_l.indexOf(Number(prof)) != -1) {
            if ($("#pol").val() == "Мужской") {
                add_prot('Профиль медицинской помощи Пол пациента должен быть женским')
            }
        }
    }
}



//Профиль медицинской помощи возраст пациента должен быть меньше 1
function prot_17() {
    if (prof != null) {
        if (prof == '55') {
            if ((get_age() / 365) > 1) {
                add_prot('Профиль медицинской помощи возраст пациента должен быть меньше 1')
            }
        }
    }
}

//Профиль медицинской помощи возраст пациента должен быть  60 лет или более
function prot_18() {
    if (prof != null) {
        if (prof == '14') {
            if ((get_age() / 365) < 60) {
                add_prot('Профиль медицинской помощи возраст пациента должен быть  60 лет или более')
            }
        }
    }
}


//Профиль медицинской помощи возраст пациента должен быть 18 лет или более
function prot_19() {
    if (prof != null) {
        let prof_l = [29, 60, 108, 122]
        if (prof_l.indexOf(Number(prof)) != -1) {
            if ((get_age() / 365) < 18) {
                add_prot('Профиль медицинской помощи возраст пациента должен быть 18 лет или более')
            }
        }
    }
}

function prot_20() {
    p_per = document.getElementById("p_per")
    if (p_per.value == '') {
        add_prot('Не заполнен признак поступления')
    }

}

function prot_21() {
    icx = document.getElementById("icx")
    if (icx.value == '') {
        add_prot('Не заполнен исход')
    }
}

function prot_22() {
    rslt = document.getElementById("rslt")
    if (rslt.value == '') {
        add_prot('Не заполнен результат')
    }
}

function prot_23() {
    ctkom = document.getElementById("ctkom")
    if (ctkom.value == '') {
        add_prot('Не заполнен страховая компания')
    }
}

function prot_24() {
    vds = document.getElementById("vds")
    if (vds.value == '') {
        add_prot('Не заполнен источник оплаты')
    }
}


function prot_25() {
    t_pol = document.getElementById("t_pol")
    ctkom = document.getElementById("ctkom")
    if (ctkom.value != 'БЕЗ ПОЛИСА' && ctkom.value != 'БЕЗ ПОЛИСА ТФОМС ТО Г.ТЮМЕНЬ' && ctkom.value != 'ОПЛАТА ПО СЧЕТУ' 
        && ctkom.value != 'ОПЛАТА В КАССУ ЛПУ'){
        if (t_pol.value == '') {
            add_prot('Не заполнен тип полиса')
        }
    }
}

function prot_26() {
    nctp = document.getElementById("nctp")
    t_pol = document.getElementById("t_pol")
    ctkom = document.getElementById("ctkom")
    vds = document.getElementById("vds")
    if (ctkom.value != 'БЕЗ ПОЛИСА' || ctkom.value != 'БЕЗ ПОЛИСА ТФОМС ТО Г.ТЮМЕНЬ' || ctkom.value != 'ОПЛАТА ПО СЧЕТУ' 
        || ctkom.value != 'ОПЛАТА В КАССУ ЛПУ' || vds.value != 'ДМС'){
        if (nctp.value.length > 0) {
            if (nctp.value.length == 16) {
                if (t_pol.value != 'Полис ОМС единого образца') {
                    return add_prot('Не соответсвия полиса и тип полиса')
                }
            }
            else if (nctp.value.length == 9) {
                if (t_pol.value != 'Временное свидетельство, подтверждающее оформление полиса обязательного медицинского страхования') {
                    return add_prot('Не соответсвия полиса и тип полиса')
                }
            }
            else{
                if (t_pol.value != 'Полис ОМС старого образца') {
                    return add_prot('Не соответсвия полиса и тип полиса')
                }
            }
        }
    }
    
}

function prot_27(){
    let kod = []
    app.$data.sprav_list.V036List.forEach(function (data) {
        kod.push(data.sCode)
    })
    let kod_op = ''
    let opers = document.getElementById("operation_table").querySelectorAll("tr")
    for (op of opers){
        if (op.hasAttribute('style')){
            kod_op = op.childNodes[3].childNodes[0].value
        }
    }


    if (kod.indexOf(kod_op) != -1) {
        if (app.$data.history.med_dev.length == 0){
            add_prot('Заполните I.4.1.Импланты!')
        }
    }
    
}















function prot_clear() {
    let protocols = document.getElementById("protocols")
    protocols.innerHTML = ''
    app.$data.protoc = false
}

function add_prot(text) {
    var p = document.createElement("p")
    p.innerHTML = text
    let protocols = document.getElementById("protocols")
    protocols.appendChild(p)
    app.$data.protoc = true
}

function diffDates(day_one, day_two) {
    return (day_one - day_two) / (60 * 60 * 24 * 1000);
};

function get_spec() {
    var koyko_table = document.getElementById("koyko_table").querySelector("tbody").querySelectorAll("td")
    if (koyko_table.length != 0) {
        return koyko_table[4].childNodes[0].value
    }
    return null
}

function get_age() {
    var date_1 = $("#datp").val()
    var date_2 = $("#datr").val()
    var d_l_1 = date_1.split("-")
    var d_l_2 = date_2.split("-")
    var d1 = new Date(d_l_1[2], d_l_1[1], d_l_1[0])
    var d2 = new Date(d_l_2[2], d_l_2[1], d_l_2[0])
    var d_n = diffDates(d1, d2)
    return d_n
}

function graphql(query) {
    return fetch('graph_hospital/', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query })
    })
        .then(response => response.json())
        .then(data => {
            return data.data
        })
        .catch((e) => {
        })
}