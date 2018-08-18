var E = window.wangEditor
var editor = new E('#editor');
// 或者 var editor = new E( document.getElementById('editor') )
// 自定义菜单配置
editor.customConfig.menus = [
    'head',  // 标题
    'bold',  // 粗体
    'fontSize',  // 字号
    'fontName',  // 字体
    'underline',  // 下划线
    'list',  // 列表
    'justify',  // 对齐方式
    'quote',  // 引用
]
editor.create();
editor.$textContainerElem[0].style.height = "50rem";