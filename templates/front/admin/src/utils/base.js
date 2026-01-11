const base = {
    get() {
        return {
            url : "http://localhost:8080/django9062th44/",
            name: "django9062th44",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于Python的新疆特产推荐系统的设计与实现"
        } 
    }
}
export default base
