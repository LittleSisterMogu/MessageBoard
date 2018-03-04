


require(['constant'], function(constant) {

    let page = location.pathname.split('/')[2];
    if (page === '') {
        page = constant.defaultPage;
    } else {
        page = page.split('.')[0];
    }

    require([page],function(Page){
        new Page();
    });
});

