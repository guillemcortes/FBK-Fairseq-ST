cd ~/datasets/mustc/en-es/data/
sed "s/[[:punct:]]//g" train/txt/train_clean.en > train/txt/train_clean.depunct.en
sed -i "s/ \+/ /g" train/txt/train_clean.depunct.en
sed "s/[[:punct:]]//g" dev/txt/dev_clean.en > dev/txt/dev_clean.depunct.en
sed -i "s/ \+/ /g" dev/txt/dev_clean.depunct.en
sed "s/[[:punct:]]//g" tst-COMMON/txt/tst-COMMON_clean.en > tst-COMMON/txt/tst-COMMON_clean.depunct.en
sed -i "s/ \+/ /g" tst-COMMON/txt/tst-COMMON_clean.depunct.en
sed "s/[[:punct:]]//g" tst-HE/txt/tst-HE_clean.en > tst-HE/txt/tst-HE_clean.depunct.en
sed -i "s/ \+/ /g" tst-HE/txt/tst-HE_clean.depunct.en
sed "s/[[:punct:]]//g" train/txt/train_clean.es > train/txt/train_clean.depunct.es
sed -i "s/ \+/ /g" train/txt/train_clean.depunct.es
sed "s/[[:punct:]]//g" dev/txt/dev_clean.es > dev/txt/dev_clean.depunct.es
sed -i "s/ \+/ /g" dev/txt/dev_clean.depunct.es
sed "s/[[:punct:]]//g" tst-COMMON/txt/tst-COMMON_clean.es > tst-COMMON/txt/tst-COMMON_clean.depunct.es
sed -i "s/ \+/ /g" tst-COMMON/txt/tst-COMMON_clean.depunct.es
sed "s/[[:punct:]]//g" tst-HE/txt/tst-HE_clean.es > tst-HE/txt/tst-HE_clean.depunct.es
sed -i "s/ \+/ /g" tst-HE/txt/tst-HE_clean.depunct.es

