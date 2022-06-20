$(function(){
    $(".date").mask("99-99-9999")
    $(".tm").mask("99:99")
    $(".ss").mask("999-999-999 99")
    $(".vec").mask("9999")
    $(".date_m").mask("99-99-99")
  });

$(function(){
    $("#datp").change(function(){
        app.$data.history.datp = $("#datp").val()
    })

    $("#tm_otd").change(function(){
         app.$data.history.tm_otd = $("#tm_otd").val()
    })
    
    $("#datv").change(function(){
        app.$data.history.datv = $("#datv").val()
    })

    $("#datr").change(function(){
        app.$data.history.datr = $("#datr").val()
    })

    $("#npr_date").change(function(){
        app.$data.history.npr_date = $("#npr_date").val()
    })
    $("#dat_otd").change(function(){
        app.$data.history.dat_otd = $("#dat_otd").val()
    })
    // $("#tm_otd_2").change(function(){
    //     app.$data.tm_otd = $("#tm_otd_2").val()
    // })

    $("#dat_pe").change(function(){
        app.$data.history.dat_pe = $("#dat_pe").val()
    })


    $("#tm_let").change(function(){
        app.$data.history.tm_let = $("#tm_let").val()
    })

    $("#docdate").change(function(){
        app.$data.history.docdate = $("#docdate").val()
    })
    
    $("#vb_a_datv").change(function(){
        app.$data.history.vb_a_datv = $("#vb_a_datv").val()
    })

    $("#dat_l1").change(function(){
        app.$data.history.dat_l1 = $("#dat_l1").val()
    })
    
    $("#dat_l2").change(function(){
        app.$data.history.dat_l2 = $("#dat_l2").val()
    })
 
    $("#diag_date").change(function(){
        app.$data.history.diag_date = $("#diag_date").val()
    })

    $("#dt_cons").change(function(){
        app.$data.history.dt_cons = $("#dt_cons").val()
    })
    
    $("#d_prot").change(function(){
        app.$data.history.d_prot = $("#d_prot").val()
    })
    $("#naprdate").change(function(){
        app.$data.history.naprdate = $("#naprdate").val()
    })
    
    $("#mp_roj").change(function(){
        app.$data.history.mp_roj = $("#mp_roj").val()
    })
    $("#tm_otd_d").change(function(){
        app.$data.history.tm_otd_d = $("#tm_otd_d").val()
    })
    $("#ss").change(function(){
        app.$data.history.ss = $("#ss").val()
    })
    $("#vec").change(function(){
        app.$data.history.vec = $("#vec").val()
    })
    $("#wskr_date").change(function(){
        app.$data.history.wskr_date = $("#wskr_date").val()
    })

    $("#datr_p").change(function(){
        app.$data.history.datr_p = $("#datr_p").val()
    })
    
    
  });