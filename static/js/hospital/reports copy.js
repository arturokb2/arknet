
Vue.component('otdel', {
    template: `<div style="display: block;height: 150px;overflow-y: auto;" class="text-center" id="otdel"> 
    <label>Отделения</label>
    <ul>
      <li class="list-group-item" v-for="otde in spravlist.Otde">
        <input type="checkbox" :value="otde['naim']">
        {{otde['naim']}}
      </li>
    </ul>
  </div>`,
    props: ['spravlist']
})

Vue.component('date', {
    template: `<div class="text-center">
        <div><label>за период (дд.мм.гггг)</label></div>
        <label>с</label>
        <input type="date" id="date_r_1">
        <label>по</label>
        <input type="date" id="date_r_2">
        </div>`
})


Vue.component('input_s_po', {
    template: `<div class="text-center">
        <label>с</label>
        <input type="text" id="input_1" style="width:88px">
        <label>по</label>
        <input type="text" id="input_2" style="width:88px">
        </div>`
})
Vue.component('district', {
    template: `<div class="text-center">
                <select class="text-center" style="width: 230px;height: 32px;margin-bottom: 10px;margin-top: 10px;" id="rai">
                <option value="">-----</option>
                <option value="Центральный АО">1.Центральный АО</option>
                <option value="Ленинский АО">2.Ленинский АО</option>
                <option value="Калининский АО">3.Калининский АО</option>
                <option value="Восточный">4.Восточный</option>
                </select>
             </div>`
})

Vue.component('isfin', {
    template: `<div style="display: block;height: 150px;overflow-y: auto;" class="text-center" id="isfin">
    <label>По источникам финансир-я</label>
    <ul>
      <li class="list-group-item" v-for="otde in spravlist.Isfin">
        <input type="checkbox" :value="otde['naim']">
        {{otde['naim']}}
      </li>
    </ul>
  </div>`,
    props: ['spravlist']
})

Vue.component('btn', {
    props: ['btn'],
    template: `<div class="text-center" style="margin-bottom:10px">
    <div>
    <input type="text" value="" id="filename" class="mb-3">
    </div>
    <button v-bind:btn="btn" type="button" id="create_btn_reports" onclick="create_reports(event)" class="btn btn-primary btn-lg" style="padding:0">Создать отчет</button>
    </div>`
})

Vue.component('tit', {
    template: `<div class="text-center" style="margin-top: 10px;">
    {{title}}
  </div>`,
    props: ['title']

})

Vue.component('all_filter', {
    template: `<div id="menu-list">
        <ul id="filters_ul">
          <li class="list-group-item"><input type="checkbox" value="datv_filt">Период выбытия</li>
          <li class="list-group-item"><input type="checkbox" value="datp_filt">Период поступления</li>
          <li class="list-group-item"><input type="checkbox" value="otd_filt">Отделение</li>
          <li class="list-group-item"><input type="checkbox" value="prof_filt">Профиль койки</li>
          <li class="list-group-item"><input type="checkbox" value="fam_filt">Фимилия (начало фамилии)</li>
          <li class="list-group-item"><input type="checkbox" value="im_filt">Имя (начало имени)</li>
          <li class="list-group-item"><input type="checkbox" value="ot_filt">Отчество (начало отчества)</li>
          <li class="list-group-item"><input type="checkbox" value="pol_filt">Пол</li>
          <li class="list-group-item"><input type="checkbox" value="type_lgots_filt">Тип льготы</li>
          <li class="list-group-item"><input type="checkbox" value="in_t_filt">Льгота</li>
          <li class="list-group-item"><input type="checkbox" value="r_n_filt">Социальный статус</li>
          <li class="list-group-item"><input type="checkbox" value="age_group_filt">Возрастная группа</li>
          <li class="list-group-item"><input type="checkbox" value="goc_filt">Форма госпитализации</li>
          <li class="list-group-item"><input type="checkbox" value="prpg_filt">Вид госпитализации</li>
          <li class="list-group-item"><input type="checkbox" value="vrez_filt">Давность заболевания</li>
          <li class="list-group-item"><input type="checkbox" value="dskz_filt">Ds основной с ...по...</li>
          <li class="list-group-item"><input type="checkbox" value="dsc_filt">Ds сопутствующий</li>
          <li class="list-group-item"><input type="checkbox" value="dspat_filt">Ds патологоанатомический</li>
          <li class="list-group-item"><input type="checkbox" value="dson_filt">Ds онкопатологии</li>
          <li class="list-group-item"><input type="checkbox" value="ksg_osn_filt">КСГ основного Ds</li>
          <li class="list-group-item"><input type="checkbox" value="c_oksm_filt">Гражданство</li>
          <li class="list-group-item"><input type="checkbox" value="terr_filt">Территория проживания</li>
          <li class="list-group-item"><input type="checkbox" value="Регион (обл.,р-н)_filt">Регион (обл.,р-н)</li>
          <li class="list-group-item"><input type="checkbox" value="rai_in_filt">АО г.Тюмень</li>
          <li class="list-group-item"><input type="checkbox" value="cj_filt">Категория проживания</li>
          <li class="list-group-item"><input type="checkbox" value="lpy_filt">Направившее учреждение</li>
          <li class="list-group-item"><input type="checkbox" value="ctkom_filt">Страховая организация</li>
          <li class="list-group-item"><input type="checkbox" value="vds_filt">Источник покрытия затрат</li>
          <li class="list-group-item"><input type="checkbox" value="icx_filt">Исход лечения</li>
          <li class="list-group-item"><input type="checkbox" value="otdel_let_filt">Отд-е летального исхода</li>
          <li class="list-group-item"><input type="checkbox" value="kod_vra_filt">Лечащий врач</li>
          <li class="list-group-item"><input type="checkbox" value="kod_op_filt">Код операции</li>
          <li class="list-group-item"><input type="checkbox" value="pr_osob_filt">Особенность выполнения операции</li>
          <li class="list-group-item"><input type="checkbox" value="t_trv_filt">Тип травмы</li>
          <li class="list-group-item"><input type="checkbox" value="trav_ns_filt">Тип телесных повреждений</li>
          <li class="list-group-item"><input type="checkbox" value="Отметка о замене персон.данных п_filt">Отметка о замене персон.данных п</li>
          <li class="list-group-item"><input type="checkbox" value="disability_filt">Наличие закрытого листа нетрудос</li>
          <li class="list-group-item"><input type="checkbox" value="Дополнительное условие_filt">Дополнительное условие</li>
          <li class="list-group-item"><input type="checkbox" value="wskr_filt">Тип вскрытия(для умерших)</li>
          <li class="list-group-item"><input type="checkbox" value="rasxp_filt">Расхождение с патанатом.Ds</li>
          <li class="list-group-item"><input type="checkbox" value="srber_filt">Срок беременности с ..по..нед</li>
          <li class="list-group-item"><input type="checkbox" value="potd_filt">Внутрибольничный перевод</li>
          <li class="list-group-item"><input type="checkbox" value="kod_y_filt">Перевод в др. ЛПУ</li>
          <li class="list-group-item"><input type="checkbox" value="dskz_prich_filt">Причина травмы</li>
          <li class="list-group-item"><input type="checkbox" value="pr_per_filt">Причина перевода в др.ЛПУ</li>
          <li class="list-group-item"><input type="checkbox" value="time_minuts_po_filt">Длительность пребывания в ПО (мин)</li>
          <li class="list-group-item"><input type="checkbox" value="stay_in_mo_filt">Пребывание в МО (к-дн)</li>
        </ul>
  </div>`
})

Vue.component('all_input_models', {
    template: `<div id="menu-group">
    <ul id="list_data">
      <li class="list-group-item"><b>Персональные данные</b></li>
      <li class="list-group-item"><input type="checkbox" id="nib">История</li>
      <li class="list-group-item"><input type="checkbox" id="fam">Фимилия</li>
      <li class="list-group-item"><input type="checkbox" id="im">Имя</li>
      <li class="list-group-item"><input type="checkbox" id="ot">Отчество</li>
      <li class="list-group-item"><input type="checkbox" id="pol">Пол</li>
      <li class="list-group-item"><input type="checkbox" id="datp">Дата поступления</li>
      <li class="list-group-item"><input type="checkbox" id="tm_otd">Время</li>
      <li class="list-group-item"><input type="checkbox" id="datv">Дата выписки</li>
      <li class="list-group-item"><input type="checkbox" id="datv">Дата выписки</li>
      <li class="list-group-item"><input type="checkbox" id="datr">Дата рождения</li>
      <li class="list-group-item"><input type="checkbox" id="otd">Отделение</li>
      <li class="list-group-item"><input type="checkbox" id="m_roj_in">Адрес регистрации</li>
      <li class="list-group-item"><input type="checkbox" id="adr_in">Адрес регистрации</li>
      <li class="list-group-item"><input type="checkbox" id="rab">Место работы</li>
      <li class="list-group-item"><input type="checkbox" id="prof">Профессия</li>
      <li class="list-group-item"><input type="checkbox" id="r_n">Социальный статус</li>
      <li class="list-group-item"><input type="checkbox" id="in_t">Категория льготности</li>
      <li class="list-group-item"><input type="checkbox" id="lpy">Кем направлен</li>
      <li class="list-group-item"><input type="checkbox" id="npr_num">№ Направления </li>
      <li class="list-group-item"><input type="checkbox" id="npr_date">Дата направления </li>
      <li class="list-group-item"><input type="checkbox" id="alg">.Подозрениена опьянение</li>
      <li class="list-group-item"><input type="checkbox" id="goc">Госпитализация</li>
      <li class="list-group-item"><input type="checkbox" id="prpg">Обращения</li>
      <li class="list-group-item"><input type="checkbox" id="vrez">Давность заболевания</li>
      <li class="list-group-item"><input type="checkbox" id="p_per">Признак поступления</li>
      <li class="list-group-item"><b>Сведения о диагнозах</b></li>
      <li class="list-group-item"><input type="checkbox" id="dsny">Ds направив.учреждения</li>
      <li class="list-group-item"><input type="checkbox" id="ds_0">Ds при поступлении</li>
      <li class="list-group-item"><input type="checkbox" id="dsk">Ds Клинический</li>
      <li class="list-group-item"><input type="checkbox" id="dskz">Ds Клин.заключ</li>
      <li class="list-group-item"><input type="checkbox" id="ds_osl">Ds осложнения</li>
      <li class="list-group-item"><input type="checkbox" id="dsc">Ds сопутствующий</li>
      <li class="list-group-item"><input type="checkbox" id="dson">Ds онкологий</li>
      <li class="list-group-item"><input type="checkbox" id="dat_otd">отметка о дате поступления из приемного отд.</li>
      <li class="list-group-item"><input type="checkbox" id="tm_otd_d">отметка о времени поступления из приемного отд.</li>
      <li class="list-group-item"><input type="checkbox" id="icx">Исход лечения.</li>
      <li class="list-group-item"><input type="checkbox" id="rslt">Результат лечения.</li>
      <li class="list-group-item"><b>Койко-дни</b></li>
      <li class="list-group-item"><input type="checkbox" id="koy_N">Всего койко-дни</li>
      <li class="list-group-item"><input type="checkbox" id="koy_aro">В Аро</li>
      <li class="list-group-item"><input type="checkbox" id="koy_otd">В профильном отделении</li>
      <li class="list-group-item"><input type="checkbox" id="koy_prof_k">Отделение</li>
      <li class="list-group-item"><input type="checkbox" id="koy_kod">Код врача</li>
      <li class="list-group-item"><b>Операции</b></li>
      <li class="list-group-item"><input type="checkbox" id="oper_date">Дата операции</li>
      <li class="list-group-item"><input type="checkbox" id="oper_tm">Время операции</li>
      <li class="list-group-item"><input type="checkbox" id="oper_py">ПО/СТАЦ</li>
      <li class="list-group-item"><input type="checkbox" id="oper_kod_op">Код операции</li>
      <li class="list-group-item"><input type="checkbox" id="oper_goc">ПЛ/ЭК</li>
      <li class="list-group-item"><input type="checkbox" id="oper_kodx">Код хирурга</li>
      <li class="list-group-item"><input type="checkbox" id="oper_pop">Основ.опер?</li>
      <li class="list-group-item"><input type="checkbox" id="oper_pr_osob">Особ-ти операции</li>
      <li class="list-group-item"><input type="checkbox" id="oper_k_mm">К-во.биом</li>
      <li class="list-group-item"><input type="checkbox" id="oper_kodxa">1-Ассистент</li>
      <li class="list-group-item"><input type="checkbox" id="oper_kodxa1">2-Ассистент</li>
      <li class="list-group-item"><input type="checkbox" id="oper_obz">Метод.обез-я</li>
      <li class="list-group-item"><input type="checkbox" id="oper_kodan">Анестезиолог</li>
      <li class="list-group-item"><b>Клинико-стат.гр.заболев-я</b></li>
      <li class="list-group-item"><input type="checkbox" id="ksg_osn">КСГ осн.заболевания</li>
      <li class="list-group-item"><input type="checkbox" id="oopkk">Дополнительный классификатор критерии</li>
      <li class="list-group-item"><input type="checkbox" id="ksg_sop">КСГ сопут.заболевания </li>
      <li class="list-group-item"><input type="checkbox" id="iddoc">Таб.N врача для ОМС</li>
      <li class="list-group-item"><b>Осложнение</b></li>
      <li class="list-group-item"><input type="checkbox" id="oslo_tnvr">Таб.N</li>
      <li class="list-group-item"><input type="checkbox" id="oslo_date">Дата осложнения</li>
      <li class="list-group-item"><input type="checkbox" id="oslo_kod_osl">Код осложнения</li>
      <li class="list-group-item"><input type="checkbox" id="oslo_xosl">Характер осл.</li>
      <li class="list-group-item"><input type="checkbox" id="oslo_posl">Причина</li>
      <li class="list-group-item"><input type="checkbox" id="oslo_aosl">Экспертиза</li>
      <li class="list-group-item"><b>Трудоспособность</b></li>
      <li class="list-group-item"><input type="checkbox" id="trs">Трудоспособность</li>
      <li class="list-group-item"><b>Манипуляция</b></li>
      <li class="list-group-item"><input type="checkbox" id="man_date">Дата манипуляции</li>
      <li class="list-group-item"><input type="checkbox" id="man_tnvr">Таб.N врача</li>
      <li class="list-group-item"><input type="checkbox" id="man_kodmn">Код Манипуляции</li>
      <li class="list-group-item"><input type="checkbox" id="man_kol">К-во</li>
      <li class="list-group-item"><input type="checkbox" id="man_pl">Плат.Услуга?</li>
      <li class="list-group-item"><b>Переводы</b></li>
      <li class="list-group-item"><input type="checkbox" id="potd">Перевод из Отд.</li>
      <li class="list-group-item"><input type="checkbox" id="dat_pe">Дата перевода</li>
      <li class="list-group-item"><input type="checkbox" id="kod_y">Перевод в Др.ЛПУ </li>
      <li class="list-group-item"><input type="checkbox" id="pr_per">Причина перевода </li>
      <li class="list-group-item"><b>Патанатомический Ds</b></li>
      <li class="list-group-item"><input type="checkbox" id="wskr_date">Дата смерти</li>
      <li class="list-group-item"><input type="checkbox" id="tm_let">Время смерти (час.мин)</li>
      <li class="list-group-item"><input type="checkbox" id="pri">Код причины летального исхода</li>
      <li class="list-group-item"><input type="checkbox" id="ds_let_kod">Ds причины летального исхода </li>
      <li class="list-group-item"><input type="checkbox" id="wskr">Вскрытие</li>
      <li class="list-group-item"><input type="checkbox" id="dspat_kod">Ds паталогоанатомический</li>
      <li class="list-group-item"><input type="checkbox" id="rasxp">Расхождение Ds установлено</li>
      <li class="list-group-item"><input type="checkbox" id="otd_y">Умер в</li>
      <li class="list-group-item"><b>Сведения о травмах</b></li>
      <li class="list-group-item"><input type="checkbox" id="dskz_kod">Характер травмы</li>
      <li class="list-group-item"><input type="checkbox" id="details_kod">Внешние причины травмы</li>
      <li class="list-group-item"><input type="checkbox" id="t_trv">Тип травмы</li>
      <li class="list-group-item"><input type="checkbox" id="trav_ns">Травма получена в рез-те противоправных действий третьих лиц</li>
      <li class="list-group-item"><b>Полис/Документ/Снилс</b></li>
      <li class="list-group-item"><input type="checkbox" id="vds">Источник оплаты</li>
      <li class="list-group-item"><input type="checkbox" id="sctp">Сер.полиса</li>
      <li class="list-group-item"><input type="checkbox" id="nctp">N полиса</li>
      <li class="list-group-item"><input type="checkbox" id="ctkom">СМО</li>
      <li class="list-group-item"><input type="checkbox" id="t_pol">Тип полиса</li>
      <li class="list-group-item"><input type="checkbox" id="udl">Тип документа</li>
      <li class="list-group-item"><input type="checkbox" id="s_pasp">Сер.ДУЛ</li>
      <li class="list-group-item"><input type="checkbox" id="n_pasp">N ДУЛ</li>
      <li class="list-group-item"><input type="checkbox" id="docdate">Дата выдачи</li>
      <li class="list-group-item"><input type="checkbox" id="docorg">Кем выдан</li>
      <li class="list-group-item"><input type="checkbox" id="m_roj">Место рождения</li>
      <li class="list-group-item"><input type="checkbox" id="ss">Снилс</li>
      <li class="list-group-item"><b>Сведения о беременности</b></li>
      <li class="list-group-item"><input type="checkbox" id="vb_a_datv">Дата</li>
      <li class="list-group-item"><input type="checkbox" id="srber">Срок беременности (недель)</li>
      <li class="list-group-item"><input type="checkbox" id="n_ber">Настоящая беременность по счету</li>
      <li class="list-group-item"><input type="checkbox" id="pria">Причины прерывания беременности</li>
      <li class="list-group-item"><input type="checkbox" id="m_prer">Метод прерывания беременности</li>
      <li class="list-group-item"><b>Лист нетрудоспособности</b></li>
      <li class="list-group-item"><input type="checkbox" id="dat_l1">Открыт с</li>
      <li class="list-group-item"><input type="checkbox" id="dat_l2">Закрыт по</li>
      <li class="list-group-item"><input type="checkbox" id="ot_ln">Закрыт</li>
      <li class="list-group-item"><input type="checkbox" id="vs_bol">Полных лет</li>
      <li class="list-group-item"><input type="checkbox" id="dis_sex_bol">Пол</li>
      <li class="list-group-item"><b>Представитель пациента</b></li>
      <li class="list-group-item"><input type="checkbox" id="fam_p">Фимилия</li>
      <li class="list-group-item"><input type="checkbox" id="im_p">Имя</li>
      <li class="list-group-item"><input type="checkbox" id="ot_p">Отчество</li>
      <li class="list-group-item"><input type="checkbox" id="pol_p">Пол</li>
      <li class="list-group-item"><input type="checkbox" id="mp_roj">Место рождения</li>
      <li class="list-group-item"><input type="checkbox" id="udl_p">Тип документа</li>
      <li class="list-group-item"><input type="checkbox" id="sp_pasp">Серия</li>
      <li class="list-group-item"><input type="checkbox" id="np_pasp">Номер</li>
      <li class="list-group-item"><input type="checkbox" id="skom_p">СМО</li>
      <li class="list-group-item"><input type="checkbox" id="stat_p">Тип полиса</li>
      <li class="list-group-item"><input type="checkbox" id="s_pol">Сер.полиса</li>
      <li class="list-group-item"><input type="checkbox" id="n_pol">N.полиса</li>
      <li class="list-group-item"><b>Карта онкобольного</b></li>
      <li class="list-group-item"><input type="checkbox" id="ds1_t">Повод обращения</li>
      <li class="list-group-item"><input type="checkbox" id="stad">Стадия заболевания</li>
      <li class="list-group-item"><input type="checkbox" id="onk_t">Стадия по T</li>
      <li class="list-group-item"><input type="checkbox" id="onk_n">Стадия по N</li>
      <li class="list-group-item"><input type="checkbox" id="onk_m">Стадия по M</li>
      <li class="list-group-item"><input type="checkbox" id="mtstz">Наличие отдельных метастазов</li>
      <li class="list-group-item"><input type="checkbox" id="c_zab">Характер заболевания</li>
      <li class="list-group-item"><b>Сведения о диагностике</b></li>
      <li class="list-group-item"><input type="checkbox" id="diag_date">Дата взятия материала</li>
      <li class="list-group-item"><input type="checkbox" id="diag_tip">Тип диагностического показателя</li>
      <li class="list-group-item"><input type="checkbox" id="diag_code">Код диагностического показателя</li>
      <li class="list-group-item"><input type="checkbox" id="diag_rslt">Код результата диагностики</li>
      <li class="list-group-item"><input type="checkbox" id="rec_rslt">Признак получения результата диагностики</li>
      <li class="list-group-item"><b>Сведения о проведении консилиума</b></li>
      <li class="list-group-item"><input type="checkbox" id="dt_cons">Дата консилиума</li>
      <li class="list-group-item"><input type="checkbox" id="pr_cons">Цель консилиума</li>
      <li class="list-group-item"><b>Сведения об услуге лечения</b></li>
      <li class="list-group-item"><input type="checkbox" id="usl_tip">Тип услуги</li>
      <li class="list-group-item"><input type="checkbox" id="hir_tip">Тип хирургического лечения</li>
      <li class="list-group-item"><b>Сведения о противопоказаниях и отказах</b></li>
      <li class="list-group-item"><input type="checkbox" id="d_prot">Дата регистрации</li>
      <li class="list-group-item"><input type="checkbox" id="prot">противопоказания и отказы</li>
      <li class="list-group-item"><b>Сведения о направлений в МО (из выписного эпикриза)</b></li>
      <li class="list-group-item"><input type="checkbox" id="naprdate">Дата направления</li>
      <li class="list-group-item"><input type="checkbox" id="napr_v">Вид направления</li>
      <li class="list-group-item"><input type="checkbox" id="napr_mo">Мо,куда рекомендовано обращаться</li>
      <li class="list-group-item"><input type="checkbox" id="napr_issl">Метод диагностич.исследования</li>
      <li class="list-group-item"><input type="checkbox" id="napr_usl">Мед.услуга(код) рекомендованная</li>
      <li class="list-group-item"><b>Мо прикрепления</b></li>
      <li class="list-group-item"><input type="checkbox" id="pmg">Мо прикрепления</li>
    </ul>
  </div>`
})


Vue.component('input_select', {
    template: `<div>
    <input type="text" v-bind:list="ll" v-bind:id="id" style="margin-bottom: 10px;" class="text-center">
    <datalist v-bind:id="ll">
    <option v-for="s in spravlist">{{s[k]}}</option>
    </datalist>
    </div>`,
    props: ['spravlist','k','ll','id']

})

// Vue.component('input_select', {
//     template: `<div>
//     <input type="text" v-bind:list="ll" style="margin-bottom: 10px;" class="text-center">
//     <datalist v-bind:id="ll">
//     <option v-for="s in spravlist">{{s[k]}}<option>
//     </datalist>
//     </div>`,
//     props: ['spravlist','k','ll']

// })

let report_oth = new Vue({

    el: '#report_oth',
    data: {
        lists_references: false,
        annual_reports: false,
        menu_list: false,
        menu_group: false,
        menu_annual: false,
        menu_reports: false,
        report_generation: false,

        //Справочники
        sprav_list: [],
        otdel: false,

        //Отчеты
        g_oth_1: false,
        g_oth_2: false,
        g_oth_3: false,
        g_oth_4: false,
        g_oth_5: false,
        g_oth_6: false,
        g_oth_7: false,
        g_oth_8: false,
        g_oth_9: false,
        g_oth_10: false,
        g_oth_11: false,
        g_oth_12: false,
        g_oth_13: false,
        g_oth_14: false,
        g_oth_15: false,
        g_oth_16: false,
        g_oth_17: false,
        g_oth_18: false,
        g_oth_19: false,
        g_oth_20: false,
        g_oth_21: false,
        g_oth_22: false,
        g_oth_23: false,
        g_oth_24: false,
        g_oth_25: false,

        a_oth_1: false,
        a_oth_2: false,
        a_oth_3: false,
        a_oth_4: false,
        a_oth_5: false,
        a_oth_6: false,
        a_oth_7: false,
        a_oth_8: false,
        a_oth_9: false,
        a_oth_10: false,
        a_oth_11: false,
        a_oth_12: false,
        a_oth_13: false,
        a_oth_14: false,
        a_oth_15: false,
        a_oth_16: false,
        a_oth_17: false,
        a_oth_18: false,
        a_oth_19: false,
        a_oth_20: false,
        a_oth_21: false,
        a_oth_22: false,
        a_oth_23: false,
        a_oth_24: false,
        a_oth_25: false,
        a_oth_26: false,
        a_oth_27: false,
        a_oth_28: false,
        a_oth_29: false,
        a_oth_30: false,
        a_oth_31: false,
        a_oth_32: false,
        a_oth_33: false,


        g_tip_ot_3_2_v: false,
        gla_vra:false,
        isfin_l:false

    },
    mounted: function () {
        this.get_sprav_list()
    },
    methods: {
        get_sprav_list: function () {
            let query = `
       query{
           Otde{
             naim
           },
           Isfin{
            naim
           },
           V020{
            kPrname
          },
          V005{
            polname
          },
          T004{
            name
          },
          RabNer{
            naim
          },
          AgeGroup{
            name
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
          Oksm{
            naim
           },
           F003{
            naim
          },
          Skom{
            naim
         },
         Isfin{
            naim
         },
         V012{
            idIz
            izName
           },
           Vra{
            kod
          },
          V001{
            kod
         },
         PROsob{
            kod
            naim
        },
        Trv{
            naim
         },
         Trvnas{
            naim
         },
         AbObsh{
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
                    this.sprav_list = data.data
                })
                .catch((e) => {
                    // console.log(e)
                })
        },
        init: function () {
            this.lists_references = false
            this.annual_reports = false
            this.menu_list = false
            this.menu_group = false
            this.menu_annual = false
            this.menu_reports = false
            this.report_generation = false
        },
        init_oth: function () {
            this.otdel = false

            this.g_oth_1 = false
            this.g_oth_2 = false
            this.g_oth_3 = false
            this.g_oth_4 = false
            this.g_oth_5 = false
            this.g_oth_6 = false
            this.g_oth_7 = false
            this.g_oth_8 = false
            this.g_oth_9 = false
            this.g_oth_10 = false
            this.g_oth_11 = false
            this.g_oth_12 = false
            this.g_oth_13 = false
            this.g_oth_14 = false
            this.g_oth_15 = false
            this.g_oth_16 = false
            this.g_oth_17 = false
            this.g_oth_18 = false
            this.g_oth_19 = false
            this.g_oth_20 = false
            this.g_oth_21 = false
            this.g_oth_22 = false
            this.g_oth_23 = false
            this.g_oth_24 = false
            this.g_oth_25 = false

            this.a_oth_1 = false
            this.a_oth_2 = false
            this.a_oth_3 = false
            this.a_oth_4 = false
            this.a_oth_5 = false
            this.a_oth_6 = false
            this.a_oth_7 = false
            this.a_oth_8 = false
            this.a_oth_9 = false
            this.a_oth_10 = false
            this.a_oth_11 = false
            this.a_oth_12 = false
            this.a_oth_13 = false
            this.a_oth_14 = false
            this.a_oth_15 = false
            this.a_oth_16 = false
            this.a_oth_17 = false
            this.a_oth_18 = false
            this.a_oth_19 = false
            this.a_oth_20 = false
            this.a_oth_21 = false
            this.a_oth_22 = false
            this.a_oth_23 = false
            this.a_oth_24 = false
            this.a_oth_25 = false
            this.a_oth_26 = false
            this.a_oth_27 = false
            this.a_oth_28 = false
            this.a_oth_29 = false
            this.a_oth_30 = false
            this.a_oth_31 = false
            this.a_oth_32 = false
            this.a_oth_33 = false

        },
        references: function () {
            this.init()
            this.init_oth()

            this.lists_references = !this.lists_references
            this.annual_reports = false
            this.menu_reports = false
            this.menu_group = false
            this.menu_annual = false


        },
        reports: function () {
            this.init()
            this.init_oth()

            this.annual_reports = !this.annual_reports
            this.lists_references = false
            this.menu_group = false
            this.menu_annual = false
            this.report_generation = false
            this.menu_reports = false

        },
        group: function () {
            this.init_oth()
            this.menu_group = !this.menu_group
            this.menu_annual = false
        },
        annual: function () {
            this.init_oth()
            this.menu_annual = !this.menu_annual
            this.menu_group = false
        },
        generation: function () {
            this.report_generation = !this.report_generation
            this.menu_reports = false
        },
        reports_menu: function () {
            this.menu_reports = !this.menu_reports
            this.report_generation = false
        },

        group_oth_1: function () {
            this.init_oth()
            this.g_oth_1 = true
        },
        group_oth_2: function () {
            this.init_oth()
            this.g_oth_2 = true
            setTimeout(() => {
                all_filters()
            }, 300);
        },
        group_oth_3: function () {
            this.init_oth()
            this.g_oth_3 = true
        },
        group_oth_4: function () {
            this.init_oth()
            this.g_oth_4 = true
            setTimeout(() => {
                all_filters()
            }, 300);
        },
        group_oth_5: function () {
            this.init_oth()
            this.g_oth_5 = true
        },
        group_oth_6: function () {
            this.init_oth()
            this.g_oth_6 = true
        },
        group_oth_7: function () {
            this.init_oth()
            this.g_oth_7 = true
        },
        group_oth_8: function () {
            this.init_oth()
            this.g_oth_8 = true
        },
        group_oth_9: function () {
            this.init_oth()
            this.g_oth_9 = true
        },
        group_oth_10: function () {
            this.init_oth()
            this.g_oth_10 = true
        },
        group_oth_11: function () {
            this.init_oth()
            this.g_oth_11 = true
        },
        group_oth_12: function () {
            this.init_oth()
            this.g_oth_12 = true
        },
        group_oth_13: function () {
            this.init_oth()
            this.g_oth_13 = true
        },
        group_oth_14: function () {
            this.init_oth()
            this.g_oth_14 = true
        },
        group_oth_15: function () {
            this.init_oth()
            this.g_oth_15 = true
        },
        group_oth_16: function () {
            this.init_oth()
            this.g_oth_16 = true
        },
        group_oth_17: function () {
            this.init_oth()
            this.g_oth_17 = true
        },
        group_oth_1: function () {
            this.init_oth()
            this.g_oth_1 = true
        },
        group_oth_18: function () {
            this.init_oth()
            this.g_oth_18 = true
        },
        group_oth_19: function () {
            this.init_oth()
            this.g_oth_19 = true
        },
        group_oth_20: function () {
            this.init_oth()
            this.g_oth_20 = true
        },
        group_oth_21: function () {
            this.init_oth()
            this.g_oth_21 = true
        },
        group_oth_22: function () {
            this.init_oth()
            this.g_oth_22 = true
        },
        group_oth_23: function () {
            this.init_oth()
            this.g_oth_23 = true
        },
        group_oth_24: function () {
            this.init_oth()
            this.g_oth_24 = true
        },
        group_oth_25: function () {
            this.init_oth()
            this.g_oth_25 = true
        },


        annual_oth_1: function () {
            this.init_oth()
            this.a_oth_1 = true
        },
        annual_oth_2: function () {
            this.init_oth()
            this.a_oth_2 = true
        },
        annual_oth_3: function () {
            this.init_oth()
            this.a_oth_3 = true
        },
        annual_oth_4: function () {
            this.init_oth()
            this.a_oth_4 = true
        },
        annual_oth_5: function () {
            this.init_oth()
            this.a_oth_5 = true
        },
        annual_oth_6: function () {
            this.init_oth()
            this.a_oth_6 = true
        },
        annual_oth_7: function () {
            this.init_oth()
            this.a_oth_7 = true
        },
        annual_oth_8: function () {
            this.init_oth()
            this.a_oth_8 = true
        },
        annual_oth_9: function () {
            this.init_oth()
            this.a_oth_9 = true
        },
        annual_oth_10: function () {
            this.init_oth()
            this.a_oth_10 = true
        },
        annual_oth_11: function () {
            this.init_oth()
            this.a_oth_11 = true
        },
        annual_oth_12: function () {
            this.init_oth()
            this.a_oth_12 = true
        },
        annual_oth_13: function () {
            this.init_oth()
            this.a_oth_13 = true
        },
        annual_oth_14: function () {
            this.init_oth()
            this.a_oth_14 = true
        },
        annual_oth_15: function () {
            this.init_oth()
            this.a_oth_15 = true
        },
        annual_oth_16: function () {
            this.init_oth()
            this.a_oth_16 = true
        },
        annual_oth_17: function () {
            this.init_oth()
            this.a_oth_17 = true
        },
        annual_oth_18: function () {
            this.init_oth()
            this.a_oth_18 = true
        },
        annual_oth_19: function () {
            this.init_oth()
            this.a_oth_19 = true
        },
        annual_oth_20: function () {
            this.init_oth()
            this.a_oth_20 = true
        },
        annual_oth_21: function () {
            this.init_oth()
            this.a_oth_21 = true
        },
        annual_oth_22: function () {
            this.init_oth()
            this.a_oth_22 = true
        },
        annual_oth_23: function () {
            this.init_oth()
            this.a_oth_23 = true
        },
        annual_oth_24: function () {
            this.init_oth()
            this.a_oth_24 = true
        },
        annual_oth_25: function () {
            this.init_oth()
            this.a_oth_25 = true
        },
        annual_oth_26: function () {
            this.init_oth()
            this.a_oth_26 = true
        },
        annual_oth_27: function () {
            this.init_oth()
            this.a_oth_27 = true
        },
        annual_oth_28: function () {
            this.init_oth()
            this.a_oth_28 = true
        },
        annual_oth_29: function () {
            this.init_oth()
            this.a_oth_29 = true
        },
        annual_oth_30: function () {
            this.init_oth()
            this.a_oth_30 = true
        },
        annual_oth_31: function () {
            this.init_oth()
            this.a_oth_31 = true
        },
        annual_oth_32: function () {
            this.init_oth()
            this.a_oth_32 = true
        },
        annual_oth_33: function () {
            this.init_oth()
            this.a_oth_33 = true
        }

    }

})


function init() {
    report_oth.init()
    report_oth.init_oth()
}

function onchange_g_select_tip_ot_1(event) {
    if (event.target.value == 'по отделению') {
        report_oth.$data.otdel = true
    }
    else {
        report_oth.$data.otdel = false
    }

    if (event.target.value == 'Для зам.гл.врача'){
        report_oth.$data.gla_vra = true
    }
    else {
        report_oth.$data.gla_vra = false
    }
}

function onchange_g_select_tip_ot_3_1(event) {
    if (event.target.value == 'по подразделениям ЛУ') {
        report_oth.$data.g_tip_ot_3_2_v = true
    }
    else {
        report_oth.$data.g_tip_ot_3_2_v = false
    }
}

function onchange_g_isfin(event) {
    if (event.target.value == 'по источникам финансир-я') {
        report_oth.$data.isfin_l = true
    }
    else {
        report_oth.$data.isfin_l = false
    }
}




function all_filters() {
    let list_li = document.getElementById("filters_ul").querySelectorAll('li')
    let filters = document.getElementById("filters")
    let type_lgots = ['Территориальная', 'Федеральная']
    for (let li of list_li) {
        li.firstChild.addEventListener("click", function () {
            let div_title = document.createElement("div")
            div_title.setAttribute("id", this.value + "_title")
            let label = document.createElement("label")
            label.innerHTML = this.nextSibling.nodeValue
            div_title.appendChild(label)

            let div_block = document.createElement("div")
            div_block.setAttribute("id", this.value + "_block")

            if (this.value == 'datv' || this.value == 'datp' || this.value == 'dskz' || this.value == 'dsc'
                || this.value == 'dspat' || this.value == 'dson' || this.value == 'srber' || this.value == 'dskz_prich') {
                let dat_1 = document.createElement("input")
                dat_1.setAttribute("style", "width:88px")
                let dat_2 = document.createElement("input")
                dat_2.setAttribute("style", "width:88px")
                let lab_1 = document.createElement("label")
                lab_1.innerHTML = 'C'
                let lab_2 = document.createElement("label")
                lab_2.innerHTML = 'по'
                div_block.appendChild(lab_1)
                div_block.appendChild(dat_1)
                div_block.appendChild(lab_2)
                div_block.appendChild(dat_2)
            }
            else if (this.value == 'otd' || this.value == 'prof_k' || this.value == 'pol' || this.value == 'type_lgots'
                || this.value == 'in_t' || this.value == 'r_n' || this.value == 'age_group' || this.value == 'goc'
                || this.value == 'prpg' || this.value == 'vrez' || this.value == 'c_oksm' || this.value == 'terr'
                || this.value == 'rai_in' || this.value == 'cj' || this.value == 'lpy' || this.value == 'ctkom'
                || this.value == 'vds' || this.value == 'icx' || this.value == 'otdel_let' || this.value == 'kod_vra'
                || this.value == 'kod_op' || this.value == 'pr_osob' || this.value == 't_trv' || this.value == 'trav_ns'
                || this.value == 'wskr' || this.value == 'rasxp' || this.value == 'potd' || this.value == 'kod_y'
                || this.value == 'pr_per') {
                var inp = document.createElement("input")
                var dat_l = document.createElement("datalist")
                if (this.value == 'otd') {
                    inp.setAttribute("list", "otdel_l")
                    dat_l.setAttribute("id", "otdel_l")
                    var list = report_oth.$data.sprav_list.Otde
                }
                else if (this.value == 'prof_k') {
                    inp.setAttribute("list", "prof_k_l")
                    dat_l.setAttribute("id", "prof_k_l")
                    var list = report_oth.$data.sprav_list.V020
                }
                else if (this.value == 'pol') {
                    inp.setAttribute("list", "pol_l")
                    dat_l.setAttribute("id", "pol_l")
                    var list = report_oth.$data.sprav_list.V005
                }
                else if (this.value == 'type_lgots') {
                    inp.setAttribute("list", "type_lgots_l")
                    dat_l.setAttribute("id", "type_lgots_l")
                    var list = type_lgots
                }
                else if (this.value == 'in_t') {
                    inp.setAttribute("list", "in_t_l")
                    dat_l.setAttribute("id", "in_t_l")
                    var list = report_oth.$data.sprav_list.T004
                }
                else if (this.value == 'r_n') {
                    inp.setAttribute("list", "r_n_l")
                    dat_l.setAttribute("id", "r_n_l")
                    var list = report_oth.$data.sprav_list.RabNer
                }
                else if (this.value == 'age_group') {
                    inp.setAttribute("list", "age_group_l")
                    dat_l.setAttribute("id", "age_group_l")
                    var list = report_oth.$data.sprav_list.AgeGroup
                }
                else if (this.value == 'goc') {
                    inp.setAttribute("list", "goc_l")
                    dat_l.setAttribute("id", "goc_l")
                    var list = report_oth.$data.sprav_list.V014
                }
                else if (this.value == 'prpg') {
                    inp.setAttribute("list", "prpg_l")
                    dat_l.setAttribute("id", "prpg_l")
                    var list = report_oth.$data.sprav_list.Prpg
                }
                else if (this.value == 'vrez') {
                    inp.setAttribute("list", "vrez_l")
                    dat_l.setAttribute("id", "vrez_l")
                    var list = report_oth.$data.sprav_list.Vrzb
                }
                else if (this.value == 'c_oksm') {
                    inp.setAttribute("list", "c_oksm_l")
                    dat_l.setAttribute("id", "c_oksm_l")
                    var list = report_oth.$data.sprav_list.Oksm
                }
                else if (this.value == 'terr') {
                    inp.setAttribute("list", "terr_l")
                    dat_l.setAttribute("id", "terr_l")
                    var list = ['г.Тюменю', '1 Юг Тюм.обл.кроме Тюм.р-н', '2 Тюменский р-н', '3 Ханты-Мансйский АО',
                        '4 Ямало-Немецкий АО', '5 Др.регионы Россий', 'Др. государства']
                }
                else if (this.value == 'rai_in') {
                    inp.setAttribute("list", "rai_in_l")
                    dat_l.setAttribute("id", "rai_in_l")
                    var list = ['Центральный АО', 'Ленинский АО', 'Калининский АО', 'Восточный АО']
                }
                else if (this.value == 'cj') {
                    inp.setAttribute("list", "cj_l")
                    dat_l.setAttribute("id", "cj_l")
                    var list = ['Городской', 'Сельский']
                }
                else if (this.value == 'lpy') {
                    inp.setAttribute("list", "lpy_l")
                    dat_l.setAttribute("id", "lpy_l")
                    var list = report_oth.$data.sprav_list.F003
                }
                else if (this.value == 'ctkom') {
                    inp.setAttribute("list", "ctkom_l")
                    dat_l.setAttribute("id", "ctkom_l")
                    var list = report_oth.$data.sprav_list.Skom
                }
                else if (this.value == 'vds') {
                    inp.setAttribute("list", "vds_l")
                    dat_l.setAttribute("id", "vds_l")
                    var list = report_oth.$data.sprav_list.Isfin
                }
                else if (this.value == 'icx') {
                    inp.setAttribute("list", "icx_l")
                    dat_l.setAttribute("id", "icx_l")
                    var list = report_oth.$data.sprav_list.V012
                }
                else if (this.value == 'otdel_let') {
                    inp.setAttribute("list", "otdel_let_l")
                    dat_l.setAttribute("id", "otdel_let_l")
                    var list = ['Отделение по поступлению', 'Приемное', 'АРО1(Анестезия и рем)', 'АРО2(Интен.,невролог.)',
                        'АРО2(Нейрореанимация)', 'АРО3']
                }
                else if (this.value == 'kod_vra') {
                    inp.setAttribute("list", "kod_vra_l")
                    dat_l.setAttribute("id", "kod_vra_l")
                    var list = report_oth.$data.sprav_list.Vra
                }
                else if (this.value == 'kod_op') {
                    inp.setAttribute("list", "kod_op_l")
                    dat_l.setAttribute("id", "kod_op_l")
                    var list = report_oth.$data.sprav_list.V001
                }
                else if (this.value == 'pr_osob') {
                    inp.setAttribute("list", "pr_osob_l")
                    dat_l.setAttribute("id", "pr_osob_l")
                    var list = report_oth.$data.sprav_list.PROsob
                }
                else if (this.value == 't_trv') {
                    inp.setAttribute("list", "t_trv_l")
                    dat_l.setAttribute("id", "t_trv_l")
                    var list = report_oth.$data.sprav_list.Trv
                }
                else if (this.value == 'trav_ns') {
                    inp.setAttribute("list", "trav_ns_l")
                    dat_l.setAttribute("id", "trav_ns_l")
                    var list = report_oth.$data.sprav_list.Trvnas
                }
                else if (this.value == 'wskr') {
                    inp.setAttribute("list", "wskr_l")
                    dat_l.setAttribute("id", "wskr_l")
                    var list = ['без вскрытия', 'патологоанатом.', 'судебное']
                }
                else if (this.value == 'rasxp') {
                    inp.setAttribute("list", "rasxp_l")
                    dat_l.setAttribute("id", "rasxp_l")
                    var list = ['да', 'нет']
                }

                else if (this.value == 'potd') {
                    inp.setAttribute("list", "potd_l")
                    dat_l.setAttribute("id", "potd_l")
                    var list = report_oth.$data.sprav_list.Otde
                }
                else if (this.value == 'kod_y') {
                    inp.setAttribute("list", "kod_y_l")
                    dat_l.setAttribute("id", "kod_y_l")
                    var list = report_oth.$data.sprav_list.F003
                }
                else if (this.value == 'pr_per') {
                    inp.setAttribute("list", "pr_per_l")
                    dat_l.setAttribute("id", "pr_per_l")
                    var list = ['для оказания специализированной мед.помощи', 'для прохождения реабилитации', 'для следующего этапа лечения']
                }

                for (o of list) {
                    var op = document.createElement("option")
                    if (this.value == 'otd') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'prof_k') {
                        op.value = o.kPrname
                        op.innerText = o.kPrname
                    }
                    else if (this.value == 'pol') {
                        op.value = o.polname
                        op.innerText = o.polname
                    }
                    else if (this.value == 'type_lgots') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'in_t') {
                        op.value = o.name
                        op.innerText = o.name
                    }
                    else if (this.value == 'r_n') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'age_group') {
                        op.value = o.name
                        op.innerText = o.name
                    }
                    else if (this.value == 'goc') {
                        op.value = o.tipName
                        op.innerText = o.tipName
                    }
                    else if (this.value == 'prpg') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'vrez') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'c_oksm') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'terr') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'rai_in') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'cj') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'lpy') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'ctkom') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'vds') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'icx') {
                        op.value = o.idIz + ' ' + o.izName
                        op.innerText = o.idIz + ' ' + o.izName
                    }
                    else if (this.value == 'otdel_let') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'kod_vra') {
                        op.value = o.kod
                        op.innerText = o.kod
                    }
                    else if (this.value == 'kod_op') {
                        op.value = o.kod
                        op.innerText = o.kod
                    }
                    else if (this.value == 'pr_osob') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 't_trv') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'trav_ns') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'wskr') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'rasxp') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'potd') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'kod_y') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'pr_per') {
                        op.value = o
                        op.innerText = o
                    }

                    dat_l.appendChild(op)
                }
                if (this.value == 'potd' || this.value == 'kod_y') {
                    var op = document.createElement("option")
                    op.value = 'все переводы'
                    op.innerText = 'все переводы'
                }
                dat_l.appendChild(op)
                div_block.appendChild(inp)
                div_block.appendChild(dat_l)
            }

            else if (this.value == 'fam' || this.value == 'im' || this.value == 'ot' || this.value == 'ksg_osn'
                || this.value == 'time_minuts_po' || this.value == 'stay_in_mo') {
                var inp = document.createElement("input")
                div_block.appendChild(inp)
            }
            else if (this.value == 'disability') {
                var lab = document.createElement("label")
                lab.innerHTML = "Поиск по нетрудоспособности"
                div_block.appendChild(lab)
            }


            if (this.checked) {
                filters.appendChild(div_title)
                filters.appendChild(div_block)

            }
            else {
                filters.removeChild(document.getElementById(this.value + "_title"))
                filters.removeChild(document.getElementById(this.value + "_block"))
            }
        })
    }
}


function create_reports(event) {
    let list_data = get_checked_input(document.getElementById("list_data"))
    let date_1 = document.getElementById("date_r_1")
    let date_2 = document.getElementById("date_r_2")

    var formData = new FormData()
    formData.append('task_type','kcc_cb')
    formData.append('date_1',date_1.value)
    formData.append('date_2',date_2.value)

    if (list_data.length > 0){
        formData.append('list_data',JSON.stringify(list_data))
    }
    
    sendRequest_f(formData)


}

function sendRequest_f(formData) {
    var r = sendRequest('reports/', 'post', formData)
    .then(response => {
        console.log(response.data.rez)
    })
    .catch(error => {
        })
}

function get_checked_input(ul) {
    if (ul != null && ul != undefined){
        let list_input = ul.querySelectorAll("input")
        let checked_input = []
        for (input of list_input){
            if (input.checked){
                checked_input.push(input.id)
            }
        }
        return checked_input
    }
    return ''

}