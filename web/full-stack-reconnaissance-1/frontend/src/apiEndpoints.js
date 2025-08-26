const MainDomain = import.meta.env.VITE_BACKEND_URL;

const APIEndpoints = {
  mainOnly: `${MainDomain}`,
  testAPI: `${MainDomain}/test`,
  loginAPI: `${MainDomain}/login`,
  logoutAPI: `${MainDomain}/logout`,
  profileAPI: `${MainDomain}/profile`,
  sProfileAPI: `${MainDomain}/sprofile`,
  registerAPI: `${MainDomain}/register`,
};

export default APIEndpoints;
