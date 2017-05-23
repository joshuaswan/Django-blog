/**
 * Created by joshua on 2017/5/23.
 */
var app = new Vue({
    el: '#app',
    data: {
        testCases: [],
        saveStatus: "",
        methods: [
            {text: 'GET', value: 0},
            {text: 'POST', value: 1},
            {text: 'PUT', value: 2},
            {text: 'DELETE', value: 3}
        ],
        versions: [],
        host_ports: [],
        execute: '',
        checked: []
    },
    methods: {
        newTestCase: function () {
            console.log("新增测试用例");
            this.testCases.push({
                case_name: '',
                host_port: this.host_ports[0],
                path: '/',
                method: 0,
                version: this.versions[0],
                expect_result: '',
            });
        },
        checkAll: function () {

        },
        deleteTestCase: function (e) {
            console.log("删除测试用例");
            console.log(e);
            for (var i = 0; i < this.testCases.length; i++) {
                var test = this.testCases[i];
                console.log("versionTemp : " + test);
                if (test === e) {
                    this.testCases.splice(i, 1)
                }
            }
        },
        allTestCase: function () {
            this.$nextTick(function () {
                this.$http.get('/maintain/getTestCase').then(function (res) {
                    if (res.data.length === 0) {
                        console.log("返回数据为空");
                        this.testCases = [
                            {
                                case_name: '用例名称',
                                host_port: this.host_ports[0],
                                path: '/',
                                method: 0,
                                version: this.versions[0],
                                expect_result: ''
                            }
                        ];
                        this.saveStatus = "获取0个版本信息，新增默认测试用例"
                    } else {
                        console.log("返回数据非空");
                        for (result in res.data) {
                            console.log(res.data[result].fields);
                            testCase = res.data[result].fields;
                            console.log(testCase.version);
                            console.log(app.selectVersion(testCase.version));
                            testCase.version = app.selectVersion(testCase.version);
                            console.log(app.selectHostPort(testCase.host_port));
                            testCase.host_port = app.selectHostPort(testCase.host_port);
                            testCase.case_id = res.data[result].pk;
                            this.testCases.push(res.data[result].fields)
                        }
                        this.saveStatus = "获取" + (parseInt(result) + 1) + "个测试用例！";
                        console.log(res.data);
                    }
                })
            })
        },
        selectVersion: function (index) {
            console.log(this.versions[0])
            for (version in this.versions) {
                if (this.versions[version].id === index)
                    return this.versions[version];
            }
            return null;
        },
        saveTestCase: function () {
            this.$nextTick(function () {
                console.log(this.versions);
                this.$http.post('/maintain/saveTestCase', this.testCases).then(function (res) {
                    console.log(res);
                    this.saveStatus = "保存测试用例正常！"
                })
            })
        },
        initVersion: function () {
            this.$nextTick(function () {
                this.$http.get('/maintain/getVersion').then(function (res) {
                    for (result in res.data) {
                        console.log(res.data[result].fields);
                        version = res.data[result].fields;
                        version.id = res.data[result].pk;
                        this.versions.push(res.data[result].fields)
                    }
                })
            })
        },
        initHostPort: function () {
            this.$nextTick(function () {
                this.$http.get('/maintain/getHostPort').then(function (res) {
                    for (result in res.data) {
                        console.log(res.data[result].fields);
                        host_port = res.data[result].fields;
                        host_port.id = res.data[result].pk;
                        this.host_ports.push(res.data[result].fields)
                    }
                })
            })
        },
        selectHostPort: function (index) {
            console.log(this.host_ports[0])
            for (hp in this.host_ports) {
                if (this.host_ports[hp].id === index)
                    return this.host_ports[hp];
            }
            return null;
        },
        runTestCases: function () {
            this.$nextTick(function () {
                this.$http.post('/action/runTestCases', this.testCases).then(function (res) {
                    this.saveStatus = "执行测试用例正常！"
                })
            })
        }
    }
});
app.initHostPort();
app.initVersion();
app.allTestCase();
