export default {
    state: {
      reading: "",
    },
    mutations: {
        updateBlog(state, data) {
            state.reading = data.reading;
        },
    },
    actions: {
        blog(context, blog) {
            context.commit('updateBlog', blog);
        },
    },
    modules: {},
    }