import datetime
from sqlalchemy import func
from flask import (render_template,
                   Blueprint,
                   redirect,
                   url_for,
                   abort)
from flask.ext.login import login_required, current_user
from flask.ext.principal import Permission, UserNeed

from webapp.extensions import poster_permission, admin_permission, cache
from webapp.models import db, Catalog, Product
from webapp.forms import CatalogForm, ProductForm

blog_blueprint = Blueprint(
    'catalog',
    __name__,
    template_folder='../templates/catalog',
    url_prefix="/catalog"
)


@blog_blueprint.route('/')
@blog_blueprint.route('/<int:page>')
@cache.cached(timeout=60)
def home(page=1):
    products = Product.query.order_by(Product.publish_date.desc()).paginate(page, 10)
    return render_template(
        'home.html',
        products=products
    )


@blog_blueprint.route('/product/<int:product_id>', methods=('GET', 'POST'))
@cache.cached(timeout=60)
def product(product_id):
    product = Product.query.get_or_404(product_id)

    return render_template(
        'product.html',
        product=product
    )