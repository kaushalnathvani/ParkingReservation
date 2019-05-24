from flask import Flask, request, jsonify


def create_app():
    app = Flask(__name__)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/api/ValidatePhoneNumber', methods=['POST'])
    def validate_number():
        params = request.form
        params = params.to_dict()
        print 'params:',params
        phone_number = params.get('phone_number', '')

        results = {'Valid': False}
        if len(phone_number) == 10:
            if phone_number[0] in ['7', '8', '9']:
                results['Valid'] = True

        return jsonify(results)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

