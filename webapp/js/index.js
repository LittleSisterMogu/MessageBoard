
define(['jquery'], function($) {
    'use strict';
    class Index{
        constructor(){
            console.log("This is index.js");
            let userName = sessionStorage.getItem('userName');
            if (userName) {
                this._renderByUserName(userName);
            } else {
                this._render();
            }
        }

        _renderByUserName(userName) {
            
        }

        _render() {
            $('body').html('test');
        }
    }

    return Index;
});
