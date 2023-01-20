// frappe.pages['bi-report'].on_page_load = function(wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'None',
// 		single_column: true
// 	});
// }

frappe.pages['bi-report'].on_page_load = function(wrapper) {
	new PageContent(wrapper);
};

PageContent = Class.extend({
	init:function(wrapper){
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: 'Equipment uptime and downtime report',
			single_column: true
		});

		this.make();
	},

	make: function(){
		let htmlContent = `
		

<div class="embed-responsive embed-responsive-16by9">
  <iframe class="embed-responsive-item" src="https://app.powerbi.com/view?r=eyJrIjoiYTgxN2NjMjQtMmY0Ny00ZDk5LWE5YmYtMDYxMjUzZWMzNzYxIiwidCI6IjYxZDFmOTk1LTkxMjgtNDhmYy1iNmFlLWE2ZDI3ZTBkZGJkMSJ9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>
</div>
		`;

		$(frappe.render_template( htmlContent, this )).appendTo(this.page.main)
	},

});