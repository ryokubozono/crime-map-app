export default {
    state: {
      user: "",
      token: "",
    },
    mutations: {
        updateUser(state, data) {
            state.user = data.user;
            state.token = data.token
        },
    },
    actions: {
        auth(context, user) {
            context.commit('updateUser', user);
        },
    },
    modules: {},
    }