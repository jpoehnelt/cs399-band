/*global module:false*/
module.exports = function (grunt) {

    // Project configuration.
    grunt.initConfig({
        // Metadata.
        meta: {
            version: '0.1.0'
        },
        banner: '/*! Beathoven - v<%= meta.version %> - ' +
            '<%= grunt.template.today("yyyy-mm-dd") %>\n' +
            '* Copyright (c) <%= grunt.template.today("yyyy") %> */\n',
        // Task configuration.
        uglify: {
            options: {
                mangle: true,
                banner: '<%= banner %>'
            },
            dist: {
                src: 'app/static/js/app.js',
                dest: 'app/static/js/app.min.js'
            }
        },
        watch: {
            js: {
                files: ['app/static/js/app.js', 'Gruntfile.js'],
                tasks: ['uglify']
            },
            css: {
                files: ['app/static/css/beathoven.css', 'Gruntfile.js'],
                tasks: ['cssmin']
            }
        },
        cssmin: {
            target: {
                files: [
                    {
                        expand: true,
                        cwd: 'app/static/css',
                        src: ['*.css', '!*.min.css'],
                        dest: 'app/static/css',
                        ext: '.min.css'
                    }
                ]
            }
        }
    });

    // These plugins provide necessary tasks.
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task.
    grunt.registerTask('default', ['uglify', 'cssmin']);

};
