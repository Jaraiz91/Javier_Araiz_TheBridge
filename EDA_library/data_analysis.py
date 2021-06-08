

# Univariate analysis

# Categorical

 def plot_cat(var, l=8,b=5):
                      plt.figure(figsize = (l, b))
                      sns.countplot(df1[var], order = df1[var].value_counts().index)

# Continuous

def plot_cont(var, l=8,b=5):
                    plt.figure(figsize=(l, b))
                    sns.distplot(df1[var])
                    plt.xlabel(var)


# Bi-variate analysis

## Categorical-categorical

 def BVA_categorical_plot(data, tar, cat):
              '''take data and two categorical variables,
               calculates the chi2 significance between the two variables
               and prints the result with countplot & CrossTab
              '''
              #isolating the variables
              data = data[[cat,tar]][:]
              #forming a crosstab
              table = pd.crosstab(data[tar],data[cat],)
              f_obs = np.array([table.iloc[0][:].values,
              table.iloc[1][:].values])
              #performing chi2 test
              from scipy.stats import chi2_contingency
              chi, p, dof, expected = chi2_contingency(f_obs)
             #checking whether results are significant
             if p<0.05:
                  sig = True
             else:
                  sig = False
             #plotting grouped plot
             sns.countplot(x=cat, hue=tar, data=data)
             plt.title("p-value = {}n difference significant? = {}n".format(round(p,8),sig))
             #plotting percent stacked bar plot
             #sns.catplot(ax, kind='stacked')
             ax1 = data.groupby(cat)[tar].value_counts(normalize=True).unstack()
             ax1.plot(kind='bar', stacked='True',title=str(ax1))
             int_level = data[cat].value_counts()


## categorical-Continuous
def TwoSampleZ(X1, X2, sigma1, sigma2, N1, N2):
         '''
          function takes mean, standard dev., and no. of observations and returns: p-value calculated  for 2-sampled Z-Test
         '''
         from numpy import sqrt, abs, round
         from scipy.stats import norm
         ovr_sigma = sqrt(sigma1**2/N1 + sigma2**2/N2)
          z = (X1 - X2)/ovr_sigma
          pval = 2*(1 - norm.cdf(abs(z)))
          return pval

def Bivariate_cont_cat(data, cont, cat, category):
           #creating 2 samples
           x1 = data[cont][data[cat]==category][:] # all categorical features
           x2 = data[cont][~(data[cat]==category)][:] # all continuous features
           #calculating descriptives
           n1, n2 = x1.shape[0], x2.shape[0]
           m1, m2 = x1.mean(), x2.mean() # calculates mean
           std1, std2 = x1.std(), x2.mean() # calculates standard deviation
            #calculating p-values
            z_p_val = TwoSampleZ(m1, m2, std1, std2, n1, n2)
            #table
            table = pd.pivot_table(data=data, values=cont, columns=cat, aggfunc = np.mean)
            #plotting
            plt.figure(figsize = (15,6), dpi=140)
            #barplot
            plt.subplot(1,2,1)
            sns.barplot([str(category),'not {}'.format(category)], [m1, m2])
            plt.ylabel('mean {}'.format(cont))
            plt.xlabel(cat)
            plt.title(' n z-test p-value = {}n {}'.format(z_p_val,table))
            # boxplot
            plt.subplot(1,2,2)
            sns.boxplot(x=cat, y=cont, data=data)
            plt.title('categorical boxplot')


# Multi-variate analysis

def Grouped_Box_Plot(data, cont, cat1, cat2):
            #boxplot
            sns.boxplot(x=cat1, y=cont, hue=cat2, data=data, orient='v')
            plt.title('Boxplot')