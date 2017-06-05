/**
 * Created by joshua on 2017/6/5.
 */
import Vue from 'vue'
Vue.config.debug = true
import main from './components/main.vue'
new Vue({
    el: '#app',
    render: h => h(main)
})